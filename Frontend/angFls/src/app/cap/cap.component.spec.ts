import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CapComponent } from './cap.component';

describe('CapComponent', () => {
  let component: CapComponent;
  let fixture: ComponentFixture<CapComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CapComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CapComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
