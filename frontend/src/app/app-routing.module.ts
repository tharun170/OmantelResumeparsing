import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { JobDetailsComponent } from './job-details/job-details.component';
import { JobResultComponent } from './job-result/job-result.component';
import { JobListComponent } from './job-list/job-list.component';
import { JobDetailsSmComponent } from './job-details-sm/job-details-sm.component';
import { JobDetailsDeComponent } from './job-details-de/job-details-de.component';

// Define routes for your app
const routes: Routes = [
  { path: '', redirectTo: '/job-list', pathMatch: 'full' }, // Default route
  { path: 'job-details', component: JobDetailsComponent }, // Route for JobDetailsComponent
  { path: 'job-details-sm', component: JobDetailsSmComponent }, // Route for JobDetailsComponent
  { path: 'job-details-de', component: JobDetailsDeComponent }, // Route for JobDetailsComponent

  { path: 'job-result', component: JobResultComponent }, // Route for JobResultComponent
  { path: 'job-list', component: JobListComponent }, // Route for JobResultComponent
  // { path: '', redirectTo: '/jobs', pathMatch: 'full' },    // Default route
  // { path: '**', redirectTo: '/jobs' }                     // Fallback route
];
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
