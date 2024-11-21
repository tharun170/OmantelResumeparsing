import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-candidates',
  templateUrl: './candidates.component.html',
  styleUrls: ['./candidates.component.css']
})
export class CandidatesComponent implements OnInit {
  candidates: any[] = []; // Array to store candidate data

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.getBackendData(); // Fetch data on component initialization
  }

  getBackendData(): void {
    this.http.get('http://localhost:5000/candidates').subscribe(
      (response: any) => {
        // Assigning fetched data to the candidates array
        this.candidates = response.data;
        console.log('Candidates Data:', this.candidates);
      },
      (error) => {
        console.error('Error fetching candidates data:', error);
      }
    );
  }
}
