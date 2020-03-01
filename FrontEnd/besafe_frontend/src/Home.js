import React, { Component } from 'react';
import ReactPageScroller from 'react-page-scroller';
import './Home.css';
import { Navbar, Nav, Container, Row, Col, Button, Pager, Pagination } from 'react-bootstrap';
import logo from './logo.png';
import { Link } from 'react-router-dom';

import HomepageIllustration from './Assets/homepageillustration.svg';
import CarCrashIcon from './Assets/carcrashicon.svg';
import ai1icon from './Assets/AI1icon.svg';
import ai2icon from './Assets/AI2.svg';
import mapimg from './Assets/map.svg';


class Home extends Component {

        render(){
          return(<div>
                <Navbar expand="lg" fixed="top" className="navbar">
                    <Navbar.Brand onClick={()=> this.goToPage(0)} style={{color: 'white'}}><img src={logo} style={{margin: '10px'}} className="nav-logo" />
                        BeSafe
                    </Navbar.Brand>
                    <Navbar.Toggle aria-controls="basic-navbar-nav" />
                    <Navbar.Collapse id="basic-navbar-nav">
                        <Nav className="ml-auto" >
                            <Nav.Link onClick={()=> this.goToPage(1)} style={{color:'white'}}>About Us</Nav.Link>
                            <Nav.Link onClick={()=> this.goToPage(2)} style={{color:'white'}}>Contact Us</Nav.Link>
                        </Nav>
                    </Navbar.Collapse>
                </Navbar>
            </div>
        );
    }
}

export default Home;
