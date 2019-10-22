import React from 'react';
import Users from "./components/List_of_Users";
import Grous from "./components/List_of_Groups";

class App extends React.Component {
    render() {
        return (
            <div>
               <Users/>
               <Grous/>

            </div>
        );

    }
}

export default App;

