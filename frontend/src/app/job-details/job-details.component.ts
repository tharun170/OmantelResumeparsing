import { Component } from '@angular/core';
import { Router } from '@angular/router'; // Import the Router
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-job-details',
  templateUrl: './job-details.component.html',
  styleUrls: ['./job-details.component.css'],
})
export class JobDetailsComponent {
  data: any;
  isLoading = false; // Progress indicator state
  progress = 0; // Progress bar percentage
  constructor(private router: Router, private http: HttpClient) {}

  navigateBack() {
    this.router.navigate(['/job-list']);
  }
  // public resumeDetails: any;
  public resumeDetails: any = {
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

  showDetails = false;

  onDragOver(event: DragEvent) {
    event.preventDefault();
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

  onFileSelect(event: any): void {
    const file: File = event.target.files[0];
    if (file) {
      this.isLoading = true;
      this.progress = 0;
      // Simulating progress bar
      const interval = setInterval(() => {
        this.progress += 10;
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

  processFile(file: File) {
    if (file.size <= 2 * 1024 * 1024) {
      // 2MB limit
      console.log('File accepted:', file.name);
      this.showDetails = true;
    } else {
      alert('File is too large. Max size is 2MB.');
    }
  }

  openModal() {
    this.showDetails = true;
    document.body.classList.add('modal-open'); // Prevents page scrolling
  }

  closeModal() {
    this.showDetails = false;
    document.body.classList.remove('modal-open'); // Restores page scrolling
    this.router.navigate(['/job-result']);
  }
}
