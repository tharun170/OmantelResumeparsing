import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-shortlisted',
  templateUrl: './shortlisted.component.html',
  styleUrl: './shortlisted.component.css'
})
export class ShortlistedComponent {
  candidates: any[] = []; // Array to hold candidate data
  backendUrl = 'http://127.0.0.1:5000/shortlisted-candidates'; // Backend endpoint

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    // Fetch data from backend when the component initializes
    this.http.get<any>(this.backendUrl).subscribe(
      (response) => {
        this.candidates = response.data; // Assign response data to candidates array
      },
      (error) => {
        console.error('Error fetching candidates:', error);
      }
    );
  }

  formatJobId(jobId: string): string {
    // Remove numbers using regex and convert to Title Case
    return jobId
      .replace(/-\d+$/, '') // Remove the trailing numbers
      .replace(/-/g, ' ') // Replace hyphens with spaces
      .replace(/\w\S*/g, (txt) => txt.charAt(0).toUpperCase() + txt.substring(1).toLowerCase()); // Title Case
  }


  getPropensityText(score: number): string {
    if (score >= 80) return 'High';
    if (score >= 60) return 'Medium';
    return 'Low';
  }
}

