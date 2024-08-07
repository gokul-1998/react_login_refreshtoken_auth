import { useState,useEffect } from "react"

import axios from "../api/axios";
import useRefreshToken from "../hooks/useRefreshToken";

const Users = () => {
    const [users,setUsers]=useState([]);

    useEffect(()=>{
        let isMounted=true;
        const controller = new AbortController();
        const refresh=useRefreshToken();

        const getUsers= async()=>{
            try{
                const response= await axios.get("/users",{signal:controller.signal});
                console.log(response.data);
                if(isMounted){
                    setUsers(response.data);
                }
            }catch(err){
                console.log(err);
            }
        }

        getUsers();
        return()=>{
            isMounted=false;
            controller.abort();
        }


    },[])
  return (
    <article>
        <h2>USers List</h2>
        {
            users?.length?(
                <ul>
                    {users.map((user,i)=><li key={i}>
                        {user?.username}</li>)}
                </ul>
            ):<p>No users to display</p>
        }
        <button onClick={()=>refresh()}>Refresh</button>
        <br />
    </article>
  )
}

export default Users