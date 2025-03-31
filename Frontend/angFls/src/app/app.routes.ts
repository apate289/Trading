import { Routes,RouterModule } from '@angular/router';
import { CapComponent } from './cap/cap.component';
import { MapComponent } from './map/map.component';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { MessageServiceComponent } from './message-service/message-service.component';
import { HomeComponent } from './home/home.component';

export const routes: Routes = [
    { path: 'home', component: HomeComponent },
    { path: 'map', component: MapComponent },
    { path: 'cap', component: CapComponent },
    { path: 'message', component: MessageServiceComponent },
    //{ path: 'home', component: HomeComponent },
    //{ path: 'home', component: HomeComponent },
    //{ path: 'about', component: AboutComponent },
    //{ path: 'products/:id', component: ProductDetailsComponent },
    { path: '', redirectTo: '/home', pathMatch: 'full' },
    { path: '**', component: PageNotFoundComponent }, // Wildcard route for 404 errors
];


@NgModule({
    imports: [BrowserModule, RouterModule,
      //RouterModule.forRoot(routes) // routes is your array of Route objects
    ],
    providers: [],
    //exports: [RouterModule] // Ensure RouterModule is exported if in a shared module
  })

export class RoutingModule { }
