import { ComponentFixture, TestBed } from '@angular/core/testing';

import { JobResultSmComponent } from './job-result-sm.component';

describe('JobResultSmComponent', () => {
  let component: JobResultSmComponent;
  let fixture: ComponentFixture<JobResultSmComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [JobResultSmComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(JobResultSmComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
