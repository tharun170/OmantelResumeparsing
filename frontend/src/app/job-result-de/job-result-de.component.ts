import { Component } from '@angular/core';
import { Router } from '@angular/router'; // Import the Router
import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-job-result-de',
  templateUrl: './job-result-de.component.html',
  styleUrl: './job-result-de.component.css'
})
export class JobResultDeComponent {
  constructor(private router: Router, private http: HttpClient) {}
  popupMessage: string | null = null;
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
  formattedExperience: any = ''; // Variable for formatted experience

  dynamicName: string = ''; // Variable for the dynamic name
  
  showPopup(message: string): void {
    this.popupMessage = `You have ${message} this Candidate!`;
    setTimeout(() => this.closePopup(), 3000); // Auto-close after 3 seconds
  }

  closePopup(): void {
    this.popupMessage = null;
  }
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

        // Extract dynamic name after fetching the data
        this.extractNameFromSummary(this.apiResult['Short Description']);
        this.formatExperience(this.apiResult['Relevant Experience']);
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
  extractNameFromSummary(summaryText: string): void {
    // const summaryText =
    //   'Based on the resume of Tharun S C for the Data Engineer role, here is a summary:'; // Example summary
    // const nameMatch  = this.apiResult['Short Description'];
    // console.log('Summary:', summaryText);
    const nameMatch = summaryText.match(/^(\w+\s+\w+(?:\s+\w+)?)/); // Extracts the first name(s) in the text
    if (nameMatch && nameMatch[1]) {
      this.dynamicName = nameMatch[1]; // Set the extracted name
    } else {
      this.dynamicName = 'Unknown'; // Fallback name
    }

    // Format Relevant Experience
    // this.apiResult['Relevant Experience'] = this.apiResult['Relevant Experience']
    //   .replace('year as', 'Year');
  }
  formatExperience(experience: string): void {
    // const experience = this.apiResult['Relevant Experience'];
    console.log('Experience:', experience);
    const match = experience.match(/(\d+)\s*year/i); // Regex to extract the number of years

    if (match && match[1]) {
      this.formattedExperience = `${match[1]} Year`; // Format as "1 Year"
    } else {
      this.formattedExperience = 'Experience Not Available'; // Fallback if no match
    }
  }
  ngOnInit(): void {
    // Trigger the backend call when the component initializes
    this.getBackendData();
  }
}
