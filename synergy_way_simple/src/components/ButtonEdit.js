import React from 'react';

import Button from "react-bootstrap/Button";
import Jumbotron from "react-bootstrap/Jumbotron";
import TableUsers from "./TableUsers";

class DttnEdit extends React.Component {
    oneClick = () => {
    console.log("Click Edit");
  }
    render() {
         return (
             <div>
                 <Button onClick={this.oneClick} variant="secondary" size="sm">
      Edit
    </Button>
             </div>
         );
    }
}

export default  DttnEdit;