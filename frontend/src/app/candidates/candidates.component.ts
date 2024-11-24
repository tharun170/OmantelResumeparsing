import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-candidates',
  templateUrl: './candidates.component.html',
  styleUrls: ['./candidates.component.css'],
})
export class CandidatesComponent implements OnInit {
  candidates: any[] = []; // Array to store candidate data
  originalCandidates: any[] = []; // Backup for reset

  currentExperienceFilter: string = 'all';
  currentJDFilter: string = 'all';
  currentSort: string = 'reset';

  selectedProfile: any = null; // Store profile data for the modal
  showModal: boolean = false; // Modal visibility toggle

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.getBackendData(); // Fetch data on component initialization
  }

  formatJobId(jobId: string): string {
    // Remove numbers using regex and convert to Title Case
    return jobId
      .replace(/-\d+$/, '') // Remove the trailing numbers
      .replace(/-/g, ' ') // Replace hyphens with spaces
      .replace(/\w\S*/g, (txt) => txt.charAt(0).toUpperCase() + txt.substring(1).toLowerCase()); // Title Case
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

  onExperienceFilterChange(event: any): void {
    this.currentExperienceFilter = event.target.value;
    this.applyFiltersAndSorting();
  }

  onJDFilterChange(event: any): void {
    this.currentJDFilter = event.target.value;
    this.applyFiltersAndSorting();
  }

  onSortChange(event: any): void {
    this.currentSort = event.target.value;
    this.applyFiltersAndSorting();
  }

  applyFiltersAndSorting(): void {
    // Step 1: Start with the original candidate list
    let filteredCandidates = [...this.originalCandidates];

    // Step 2: Apply experience filter
    if (this.currentExperienceFilter !== 'all') {
      filteredCandidates = filteredCandidates.filter((candidate) => {
        const totalMonths = this.parseExperience(
          candidate.ai_response['Relevant Experience']
        );
        const candidateYears = totalMonths / 12; // Convert months to years
        return (
          Math.floor(candidateYears) ===
          parseInt(this.currentExperienceFilter, 10)
        );
      });
    }

    // Step 3: Apply JD filter (using job_id)
    if (this.currentJDFilter !== 'all') {
      filteredCandidates = filteredCandidates.filter((candidate) =>
        candidate.job_id.toLowerCase().includes(this.currentJDFilter.toLowerCase())
      );
    }

    // Step 4: Apply sorting
    if (this.currentSort === 'propensity') {
      filteredCandidates.sort((a, b) =>
        this.getPropensityText(b.ai_response['Relevance Score']).localeCompare(
          this.getPropensityText(a.ai_response['Relevance Score'])
        )
      );
    } else if (this.currentSort === 'relevance') {
      filteredCandidates.sort(
        (a, b) =>
          b.ai_response['Relevance Score'] - a.ai_response['Relevance Score']
      );
    } else if (this.currentSort === 'experience') {
      filteredCandidates.sort((a, b) => {
        const experienceA = this.convertExperienceToMonths(
          a.ai_response['Relevant Experience']
        );
        const experienceB = this.convertExperienceToMonths(
          b.ai_response['Relevant Experience']
        );
        return experienceB - experienceA; // Descending order
      });
    }

    // Step 5: Update the candidates list
    this.candidates = filteredCandidates;
  }

  convertExperienceToMonths(experience: string): number {
    const yearsMatch = experience.match(/(\d+)\s*years?/);
    const monthsMatch = experience.match(/(\d+)\s*months?/);

    const years = yearsMatch ? parseInt(yearsMatch[1], 10) : 0;
    const months = monthsMatch ? parseInt(monthsMatch[1], 10) : 0;

    return years * 12 + months;
  }

  parseExperience(experience: string): number {
    const match = experience.match(/^(\d+)\s*years?\s*(\d+)\s*months?$/);
    if (match) {
      const years = parseInt(match[1], 10);
      const months = parseInt(match[2], 10);
      return years * 12 + months;
    }
    return 0;
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





  viewProfile(fullName: string): void {
    // Send POST request to fetch profile info for a specific candidate
    this.http.post('http://localhost:5000/profile', { full_name: fullName }).subscribe(
      (response: any) => {
        this.selectedProfile = response; // Save profile data
        this.showModal = true; // Display modal
        console.log('Profile Data:', this.selectedProfile);
      },
      (error) => {
        console.error('Error fetching profile data:', error);
      }
    );
  }
  closeModal(): void {
    this.showModal = false; // Hide modal
    this.selectedProfile = null; // Clear profile data
  }
  closeModalOnOutsideClick(event: MouseEvent): void {
    const target = event.target as HTMLElement;
  
    // Check if the click is outside the modal content
    if (target.classList.contains('modal-overlay')) {
      this.closeModal(); // Close the modal
    }
  }
  
}
