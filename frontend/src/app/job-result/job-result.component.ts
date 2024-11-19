import { Component } from '@angular/core';
import { Router } from '@angular/router'; // Import the Router
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-job-result',
  templateUrl: './job-result.component.html',
  styleUrl: './job-result.component.css',
})
export class JobResultComponent {
  constructor(private router: Router, private http: HttpClient) {}
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
  public apiResult: any = {
    'Relevance Score': null,
    'Relevant Experience': '',
    'Short Description': '',
    id: '',
    message: '',
  };
  showDetails = false;

  // fetchApiResult() {
  //   this.http.get('http://localhost:5000/submit').subscribe(
  //     (response: any) => {
  //       this.apiResult = {
  //         'Relevance Score': response.result['Relevance Score'],
  //         'Relevant Experience': response.result['Relevant Experience'],
  //         'Short Description': response.result['Short Description'],
  //         id: response.id,
  //         message: response.message,
  //       };
  //       console.log('API Result:', this.apiResult);
  //     },
  //     (error) => {
  //       console.error('Error fetching API result:', error);
  //     }
  //   );
  // }

  getBackendData(): void {
    this.http.get('http://localhost:5000/submit').subscribe(
      (response: any) => {
        this.apiResult = {
          'Relevance Score': response.result['Relevance Score'],
          'Relevant Experience': response.result['Relevant Experience'],
          'Short Description': response.result['Short Description'],
          id: response.id,
          message: response.message,
        };
        console.log('API Result:', this.apiResult);
      },
      (error) => {
        console.error('Error fetching API result:', error);
      }
    );
  }

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
      const formData = new FormData();
      formData.append('file', file);

      this.http.post('http://localhost:5000/upload', formData).subscribe(
        (response) => {
          this.resumeDetails = response;
          console.log('Data received:', this.resumeDetails);
          this.processFile(file);
          this.showDetails = true;
        },
        (error) => {
          console.error('Error:', error);
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
    // this.router.navigate(['/job-result']);
  }
  navigateBack() {
    this.router.navigate(['/job-list']);
  }

  ngOnInit(): void {
    // Trigger the backend call when the component initializes
    this.getBackendData();
  }
}
