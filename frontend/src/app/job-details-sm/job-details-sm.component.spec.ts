import { ComponentFixture, TestBed } from '@angular/core/testing';

import { JobDetailsSmComponent } from './job-details-sm.component';

describe('JobDetailsSmComponent', () => {
  let component: JobDetailsSmComponent;
  let fixture: ComponentFixture<JobDetailsSmComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [JobDetailsSmComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(JobDetailsSmComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
