
import React from 'react';
import Jumbotron  from 'react-bootstrap/Jumbotron';
import Button from "react-bootstrap/Button";
import TableUsers from "./TableUsers";


class JumbotronPage extends React.Component {
    render() {
         return (
             <div>
                 <Jumbotron>
  <h1>Table Users</h1>
  <TableUsers />
  <p>
    <Button variant="primary">Add User</Button>
  </p>
                 </Jumbotron>
             </div>
         );
    }
}

export default  JumbotronPage;


