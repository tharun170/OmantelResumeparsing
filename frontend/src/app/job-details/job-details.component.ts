import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { ActivatedRoute } from '@angular/router';
import { Observable } from 'rxjs/internal/Observable';

@Component({
  selector: 'app-job-details',
  templateUrl: './job-details.component.html',
  styleUrls: ['./job-details.component.css'],
})
export class JobDetailsComponent {
  data: any;
  isLoading = false;
  progress = 0;
  showDetails = false;
  jobDetails: any;
  errorMessage: string = '';
  // Dynamic job description data
  jobDescription: any = {}; // Stores dynamic job description data
  showJobDescription = false; // Controls modal visibility
  private baseUrl: string = 'http://localhost:5000/jobs'; // Flask API base URL

  // Resume details dynamically updated via ngModel
  resumeDetails: any = {
    'Full Name': '',
    Email: '',
    'Phone Number': '',
    Location: '',
    Summary: '',
    Education: [
      {
        Degree: '',
        Institution: '',
        Location: '',
        GPA: '',
        StartDate: '',
        EndDate: '',
      },
    ],
    'Work Experience': [
      {
        Company: '',
        Position: '',
        Location: '',
        StartDate: '',
        EndDate: '',
        Description: [''],
      },
    ],
    Certifications: [
      {
        Name: '',
        Organization: '',
      },
    ],
    Skills: {
      'Soft Skills': [],
      'Technical Skills': [],
    },
  };
  // jobDescription: any;

  constructor(
    private router: Router,
    private http: HttpClient,
    private route: ActivatedRoute
  ) {}

  ngOnInit() {
    // Fetch dynamic job description data from an API
    this.http.get('http://localhost:5000/jd3').subscribe(
      (response: any) => {
        this.jobDescription = response; // Bind the response to jobDescription
      },
      (error) => {
        console.error('Failed to fetch job description:', error);
      }
    );
  }
  // Open Job Description Modal
  openJobDescriptionModal() {
    // const jobId = 'data-engineer-001'; // Replace with dynamic job ID if available
    // this.fetchJobDescription(jobId);
    this.showJobDescription = true;
  }

  // Close Job Description Modal
  closeJobDescriptionModal() {
    this.showJobDescription = false;
  }

  fetchJobDetails(jobId: string): Observable<any> {
    const url = `${this.baseUrl}/${jobId}`;
    return this.http.get<any>(url);
  }
  processFile(file: File) {
    if (file.size <= 2 * 1024 * 1024) {
      // 2MB limit
      console.log('File accepted:', file.name);
      this.showDetails = true;
    } else {
      alert('File is too large. Max size is 2MB.');
    }
  }
  onDragOver(event: DragEvent) {
    event.preventDefault();
  }
  navigateBack() {
    this.router.navigate(['/job-list']);
  }

  onFileSelect(event: any): void {
    const file: File = event.target.files[0];
    if (file) {
      this.isLoading = true;
      this.progress = 0;
      // Simulating progress bar
      const interval = setInterval(() => {
        this.progress += 5;
        if (this.progress >= 100) {
          clearInterval(interval);
        }
      }, 200);
      // Adjust interval time as needed for smoother progress
      const formData = new FormData();
      formData.append('file', file);

      this.http.post('http://localhost:5000/upload', formData).subscribe(
        (response) => {
          this.resumeDetails = response;
          console.log('Data received:', this.resumeDetails);
          this.processFile(file);
          this.showDetails = true;
          this.isLoading = false; // Hide progress bar
        },
        (error) => {
          console.error('Error:', error);
          this.isLoading = false; // Hide progress bar
        }
      );
    }
  }

  onFileDrop(event: DragEvent) {
    event.preventDefault();
    if (event.dataTransfer?.files.length) {
      this.processFile(event.dataTransfer.files[0]);
    }
  }
  stopPropagation(event: MouseEvent) {
    event.stopPropagation();
  }
  openModal() {
    this.showDetails = true;
    document.body.classList.add('modal-open'); // Prevents page scrolling
  }
  closeModal() {
    // Prepare the dynamic payload
    const payload = {
      parsed_resume: {
        Certifications: this.resumeDetails.Certifications,
        Education: this.resumeDetails.Education,
        Email: this.resumeDetails.Email,
        'Full Name': this.resumeDetails['Full Name'],
        Location: this.resumeDetails.Location,
        'Phone Number': this.resumeDetails['Phone Number'],
        Skills: this.resumeDetails.Skills,
        Summary: this.resumeDetails.Summary,
        'Work Experience': this.resumeDetails['Work Experience'],
      },
      job_id: this.jobDescription.id, // Include the job ID,
    };

    // POST the payload
    this.http.post('http://localhost:5000/submit', payload).subscribe(
      (response) => {
        console.log('Response from /ai-response:', response);
        this.showDetails = false;
        document.body.classList.remove('modal-open');
        this.router.navigate(['/job-result']);
      },
      (error) => {
        console.error('Error while posting to /ai-response:', error);
        alert('An error occurred while sending the data. Please try again.');
      }
    );
  }
}
