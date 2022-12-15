import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VistaViajeComponent } from './vista-viaje.component';

describe('VistaViajeComponent', () => {
  let component: VistaViajeComponent;
  let fixture: ComponentFixture<VistaViajeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ VistaViajeComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(VistaViajeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
