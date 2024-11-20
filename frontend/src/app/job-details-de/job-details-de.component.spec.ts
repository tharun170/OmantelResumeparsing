import { ComponentFixture, TestBed } from '@angular/core/testing';

import { JobDetailsDeComponent } from './job-details-de.component';

describe('JobDetailsDeComponent', () => {
  let component: JobDetailsDeComponent;
  let fixture: ComponentFixture<JobDetailsDeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [JobDetailsDeComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(JobDetailsDeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
