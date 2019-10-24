import React from 'react';
import Table from "react-bootstrap/table";
import ButtonToolbar from "react-bootstrap/ButtonToolbar";
import BttnDel from "./ButtonDel";
import BttnEdit from "./ButtonEdit";
class TableUsers extends React.Component {
    render() {
        return (
            <div>
                <Table striped bordered hover>
  <thead>
    <tr>
      <th>Username</th>
      <th>Created</th>
      <th>Group</th>
        <th>Actions</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>TestUser</td>
      <td>12.06.2018</td>
      <td>User</td>
        <td><ButtonToolbar> <BttnEdit />  <BttnDel /> </ButtonToolbar> </td>
    </tr>
    <tr>
      <td>TestUser2</td>
      <td>15.08.2019</td>
      <td>Admin</td>
      <td></td>
    </tr>
    <tr>
      <td>TestUser3</td>
      <td colSpan="2">Larry the Bird</td>
      <td>@twitter</td>
    </tr>
  </tbody>
</Table>
            </div>
        );
    }

}
export default TableUsers;
