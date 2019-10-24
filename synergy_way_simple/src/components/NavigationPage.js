import React from 'react';
import Tab  from "react-bootstrap/Tab";
import Tabs  from "react-bootstrap/Tabs";
import JumbotronPage from "./Jumbotron";


class NavigationPage extends React.Component {
    render() {
         return (
             <div>
            <Tabs defaultActiveKey="Users" id="uncontrolled-tab-example">
  <Tab eventKey="Users" title="Users">
        <JumbotronPage />
  </Tab>
  <Tab eventKey="Groups" title="Groups">

  </Tab>
</Tabs>
             </div>
         );
    }
}

export default  NavigationPage;





