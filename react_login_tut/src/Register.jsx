import React from 'react'
import {useRef,useState,useEffect} from 'react'

import {faCheck,faTimes,faInfoCircle} from '@fortawesome/free-solid-svg-icons'
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome'

const USER_REGEX=/^[a-zA-Z][a-zA-Z0-9-_]{3,23}$/;
// overall it will be 4 to 24 characters long
const PWD_REGEX=/^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])[\w!@#\$%\^&\*]{8,24}$/;

const Register = () => {
    const userRef=useRef(null);
    const errRef=useRef(null);
    // useRefs are used to access the DOM elements directly, without using the event object, in this case, the input element and the error message element, respectively, are accessed directly, without using the event object to access them indirectly,

    const [user,setUser]=useState('');
    const [validName,setValidName]=useState(false);
    const [userFocus,setUserFocus]=useState(false);

    const [pwd,setPwd]=useState('');
    const [validPwd,setValidPwd]=useState(false);
    const [pwdFocus,setPwdFocus]=useState(false);

    const [matchPwd,setMatchPwd]=useState('');
    const [validMatch,setValidMatch]=useState(false);
    const [matchFocus,setMatchFocus]=useState(false);

    const [errMsg,setErrMsg]=useState('');
    const [success,setSuccess]=useState(false);
    

    useEffect(()=>{
        userRef.current.focus();
    },[]);
    // it going to be setting the focus when the component loads on the user input field

    useEffect(()=>{
        const result=USER_REGEX.test(user);
        console.log(result);
        console.log(user);
        setValidName(result);
    },[user]);

    useEffect(()=>{
        const result=PWD_REGEX.test(pwd);
        console.log(result);
        console.log(pwd);
        setValidPwd(result);
        const match=pwd===matchPwd;
        setValidMatch(match);
    },[pwd,matchPwd]);

    useEffect(()=>{
        setErrMsg(''); // this means that the error message is empty
    },[user,pwd,matchPwd]);


  return (
    <section>
      
    </section>
  )
}

export default Register
