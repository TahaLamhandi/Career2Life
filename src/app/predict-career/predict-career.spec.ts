import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PredictCareer } from './predict-career';

describe('PredictCareer', () => {
  let component: PredictCareer;
  let fixture: ComponentFixture<PredictCareer>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [PredictCareer]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PredictCareer);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
