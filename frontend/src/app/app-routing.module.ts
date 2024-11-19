import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { JobDetailsComponent } from './job-details/job-details.component';
import { JobResultComponent } from './job-result/job-result.component';
import { JobListComponent } from './job-list/job-list.component';

// Define routes for your app
const routes: Routes = [
  { path: '', redirectTo: '/job-list', pathMatch: 'full' }, // Default route
  { path: 'job-details', component: JobDetailsComponent }, // Route for JobDetailsComponent
  { path: 'job-result', component: JobResultComponent }, // Route for JobResultComponent
  { path: 'job-list', component: JobListComponent }, // Route for JobResultComponent
];
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
