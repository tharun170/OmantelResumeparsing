import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-candidates',
  templateUrl: './candidates.component.html',
  styleUrls: ['./candidates.component.css']
})
export class CandidatesComponent implements OnInit {
  candidates: any[] = []; // Array to store candidate data
  originalCandidates: any[] = []; // Backup for reset

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.getBackendData(); // Fetch data on component initialization
  }

  getRelevanceText(score: number): string {
    if (score >= 80) {
      return 'High';
    } else if (score >= 60) {
      return 'Medium';
    } else {
      return 'Low';
    }
  }

  getPropensityText(score: number): string {
    if (score >= 80) {
      return 'High';
    } else if (score >= 60) {
      return 'Medium';
    } else {
      return 'Low';
    }
  }

  getBackendData(): void {
    this.http.get('http://localhost:5000/candidates').subscribe(
      (response: any) => {
        this.candidates = response.data;
        this.originalCandidates = [...this.candidates]; // Backup original data
        console.log('Candidates Data:', this.candidates);
      },
      (error) => {
        console.error('Error fetching candidates data:', error);
      }
    );
  }

  // Sort methods
  sortByPropensity(): void {
    this.candidates.sort((a, b) =>
      this.getPropensityText(b.ai_response['Relevance Score']).localeCompare(
        this.getPropensityText(a.ai_response['Relevance Score'])
      )
    );
  }

  sortByRelevance(): void {
    this.candidates.sort(
      (a, b) =>
        b.ai_response['Relevance Score'] - a.ai_response['Relevance Score']
    );
  }

  sortByExperience(): void {
    this.candidates.sort((a, b) => {
      const experienceA = this.convertExperienceToMonths(a.ai_response['Relevant Experience']);
      const experienceB = this.convertExperienceToMonths(b.ai_response['Relevant Experience']);
      return experienceB - experienceA; // Descending order
    });
  }
  
  convertExperienceToMonths(experience: string): number {
    const yearsMatch = experience.match(/(\d+)\s*years?/); // Extract the number of years
    const monthsMatch = experience.match(/(\d+)\s*months?/); // Extract the number of months
  
    const years = yearsMatch ? parseInt(yearsMatch[1], 10) : 0;
    const months = monthsMatch ? parseInt(monthsMatch[1], 10) : 0;
  
    return years * 12 + months; // Total months
  }
  
  onSortChange(event: any): void {
    const selectedOption = event.target.value;
  
    if (selectedOption === 'propensity') {
      this.sortByPropensity();
    } else if (selectedOption === 'relevance') {
      this.sortByRelevance();
    } else if (selectedOption === 'experience') {
      this.sortByExperience();
    } else if (selectedOption === 'reset') {
      this.resetSorting();
    }
  }
  
  resetSorting(): void {
    this.candidates = [...this.originalCandidates];
  }
  onExperienceFilterChange(event: any): void {
    const selectedExperience = event.target.value;
    if (selectedExperience === 'all') {
      this.getBackendData(); // Fetches all candidates from the backend
    } else {
      // Apply filter based on selected experience
      this.filterByExperience(selectedExperience);
    }
  }
  
  // Function to parse the experience string like '4 years 5 months' into total months
  parseExperience(experience: string): number {
    const match = experience.match(/^(\d+)\s*years?\s*(\d+)\s*months?$/);
    if (match) {
      const years = parseInt(match[1], 10);
      const months = parseInt(match[2], 10);
      return years * 12 + months; // Total experience in months
    }
    return 0; // Default if the format is incorrect
  }
  
  // Function to filter candidates based on their total experience
  filterByExperience(years: string): void {
    const experienceFilter = parseInt(years, 10); // Convert the selected year filter value to number
    const filteredCandidates = this.candidates.filter(candidate => {
      const totalMonths = this.parseExperience(candidate.ai_response['Relevant Experience']);
      const candidateYears = totalMonths / 12; // Convert months to years
      return Math.floor(candidateYears) === experienceFilter; // Compare full years (ignoring months)
    });
    this.candidates = filteredCandidates; // Update candidates list with filtered data
  }
  onJDFilterChange(event: any): void {
    const selectedJD = event.target.value;
    if (selectedJD === 'all') {
      this.getBackendData(); // Fetches all candidates from the backend
    } else {
      // Apply filter based on selected Job Description
      this.filterByJD(selectedJD);
    }
  }
  
  filterByJD(jobDescription: string): void {
    const filteredCandidates = this.candidates.filter(candidate => {
      return candidate.parsed_resume['Job Description'].includes(jobDescription);
    });
    this.candidates = filteredCandidates; // Update candidates list with filtered data
  }
  
}
