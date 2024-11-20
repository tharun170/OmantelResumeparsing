import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';
import { HttpClientModule } from '@angular/common/http'; // Import HttpClientModule
import { JobDetailsComponent } from './job-details/job-details.component';
import { JobResultComponent } from './job-result/job-result.component';
import { JobListComponent } from './job-list/job-list.component';
import { FormsModule } from '@angular/forms';
import { JobDetailsSmComponent } from './job-details-sm/job-details-sm.component';
import { JobDetailsDeComponent } from './job-details-de/job-details-de.component';

@NgModule({
  declarations: [
    AppComponent, // Root component
    JobDetailsComponent,
    JobResultComponent,
    JobListComponent,
    JobDetailsSmComponent,
    JobDetailsDeComponent, // Other components
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule, // Essential module for running the app in a browser
    FormsModule,
  ],
  providers: [], // Services (if any)
  bootstrap: [AppComponent], // Entry point
})
export class AppModule {}
