import { useState, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import { Panel, Form, Button, Message, useToaster } from 'rsuite';
import Logo from '../../Logo/Logo';
import "./Auth.scss"
import { login } from '../../functions/api_calls';

type LogInFormData = {
  email: string;
  password: string;
}


const Login = () => {

  const navigate = useNavigate();
  const [formValue, setFormValue] = useState<LogInFormData>({
    email:"",
    password:"",
  });

  const [loading,setLoading] = useState(false);
  const formRef = useRef<any>(null);
  const toaster = useToaster();


  const handleSubmit = async() => {
    if (!formRef.current?.check()){
      return;
    }
    
    const {email, password} = formValue;

    if (!email || !password){
      toaster.push(
        <Message>Please fill in all fields</Message>,
        { placement: 'topCenter' }
      );
    }

    setLoading(true);

    try{
      const response = await login(email,password)

      if (response && response.user_ID){
        const userData = {
          user_ID : response.user_ID,
          role: response.role,
          email: email    
        }

        localStorage.setItem("sijaisx-user",JSON.stringify(userData));

        toaster.push(
          <Message type="success">Login successful! Redirecting...</Message>,
          { placement: 'topCenter' }
        );
        setTimeout(()=>{
          if(userData.role === "teacher"){
            navigate("/teacher/dashboard");
          } else if(userData.role === "substitute"){
            navigate("/substitute/dashboard");
          }else{
            navigate("/");
          }
        },1500);
      }
    }catch(error){
      console.log("Login error:",error)
      toaster.push(
        <Message type="error">Login failed. Please try again.</Message>,
        { placement: 'topCenter' }
      );
    }finally{
      setLoading(false);
    }
  };




  
  return (
    <div className="auth-container">
      <div className="auth-card">
        <div className="auth-header">
          <Logo size="large" />
          <h1>Welcome Back</h1>
          <p>Sign in to manage substitute teaching</p>
        </div>

        <Panel bordered className="auth-panel">
        <Form
          fluid
          ref={formRef}
          formValue={formValue}
          onChange={(value) => setFormValue(value as LogInFormData)}
          onSubmit={handleSubmit}
        >
            <Form.Group>
              <Form.ControlLabel>Email Address</Form.ControlLabel>
              <Form.Control name="email" type="email" placeholder="you@school.fi" />
            </Form.Group>

            <Form.Group>
              <Form.ControlLabel>Password</Form.ControlLabel>
              <Form.Control name="password" type="password" placeholder="Enter password" />
            </Form.Group>


            <Button appearance="primary" block size="lg" type="submit">
              Sign In
            </Button>
          </Form>

          <div className="auth-footer">
            <a href="/forgot-password">Forgot password?</a>
            <span>Don't have an account? <a href="/register">Register</a></span>
          </div>
        </Panel>
      </div>
    </div>
  );
};

export default Login;
