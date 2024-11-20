import { ComponentFixture, TestBed } from '@angular/core/testing';

import { JobResultDeComponent } from './job-result-de.component';

describe('JobResultDeComponent', () => {
  let component: JobResultDeComponent;
  let fixture: ComponentFixture<JobResultDeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [JobResultDeComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(JobResultDeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
