import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ShortlistedComponent } from './shortlisted.component';

describe('ShortlistedComponent', () => {
  let component: ShortlistedComponent;
  let fixture: ComponentFixture<ShortlistedComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ShortlistedComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ShortlistedComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
