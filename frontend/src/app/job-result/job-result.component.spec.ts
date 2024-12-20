import { ComponentFixture, TestBed } from '@angular/core/testing';

import { JobResultComponent } from './job-result.component';

describe('JobResultComponent', () => {
  let component: JobResultComponent;
  let fixture: ComponentFixture<JobResultComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [JobResultComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(JobResultComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
