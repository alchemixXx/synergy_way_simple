import React from 'react';

import Button from "react-bootstrap/Button";

class BttnDel extends React.Component {
    oneClick = () => {
    console.log("Click Delete");
  }
    render() {
         return (
             <div >
                 <Button onClick={this.oneClick} variant="secondary" size="sm">
      Delete
    </Button>
             </div>
         );
    }
}

export default  BttnDel;