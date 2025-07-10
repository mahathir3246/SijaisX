import { Panel, Form, Button, Input, Divider, Message, useToaster } from 'rsuite';
import { useState, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import styles from '../../scss_stylings/login.module.scss';
import { login } from '../../functions/api_calls';

type LoginFormData = {
  email: string;
  password: string;
};

const LoginForm = () => {
  const [formValue, setFormValue] = useState<LoginFormData>({
    email: '',
    password: ''
  });
  const [loading, setLoading] = useState(false);
  const formRef = useRef<any>(null);
  const toaster = useToaster();
  const navigate = useNavigate();

  const handleSubmit = async () => {
    if (!formRef.current?.check()) {
      return;
    }

    const { email, password } = formValue;
    
    if (!email || !password) {
      toaster.push(
        <Message type="error">Please fill in all fields</Message>,
        { placement: 'topCenter' }
      );
      return;
    }

    setLoading(true);
    
    try {
      const response = await login(email, password);
      
      if (response && response.user_ID) {
        // Store user data in localStorage for session management
        const userData = {
          user_ID: response.user_ID,
          role: response.role,
          email: email
        };
        
        localStorage.setItem('sijaisx_user', JSON.stringify(userData));
        
        toaster.push(
          <Message type="success">Login successful! Redirecting...</Message>,
          { placement: 'topCenter' }
        );

        // Redirect based on user role
        setTimeout(() => {
          if (response.role === 'teacher') {
            navigate('/opettajille');
          } else if (response.role === 'substitute') {
            navigate('/sijaisille');
          } else {
            navigate('/');
          }
        }, 1500);
        
      } else {
        toaster.push(
          <Message type="error">Invalid email or password</Message>,
          { placement: 'topCenter' }
        );
      }
    } catch (error) {
      console.error('Login error:', error);
      toaster.push(
        <Message type="error">Login failed. Please try again.</Message>,
        { placement: 'topCenter' }
      );
    } finally {
      setLoading(false);
    }
  };

  const handleCreateAccount = () => {
    navigate('/register');
  };

  return (
    <Panel className={styles.loginForm}>
      <h5 className={styles.header}>Welcome to SijaisX!</h5>
      <div className={styles.formClose}>
        <Button appearance="subtle" />
      </div>

      <div className={styles.loginContent}>
        <h2 className={styles.loginTitle}>Sign In</h2>
        <p className={styles.loginSubtitle}>
          Enter your credentials to access your account
        </p>

        <Form 
          fluid 
          ref={formRef}
          formValue={formValue}
          onChange={(value) => setFormValue(value as LoginFormData)}
          onSubmit={handleSubmit}
        >
          <Form.Group>
            <Form.ControlLabel>Email Address</Form.ControlLabel>
            <Form.Control
              name="email"
              type="email"
              accepter={Input}
              placeholder="Enter your email"
              disabled={loading}
            />
          </Form.Group>

          <Form.Group>
            <Form.ControlLabel>Password</Form.ControlLabel>
            <Form.Control
              name="password"
              type="password"
              accepter={Input}
              placeholder="Enter your password"
              disabled={loading}
            />
          </Form.Group>

          <Form.Group>
            <Button 
              appearance="primary" 
              size="lg" 
              block
              loading={loading}
              onClick={handleSubmit}
              type="submit"
            >
              {loading ? 'Signing In...' : 'Sign In'}
            </Button>
          </Form.Group>
        </Form>

        <Divider>or</Divider>

        <div className={styles.authSwitch}>
          <p>Don't have an account?</p>
          <Button appearance="link" onClick={handleCreateAccount}>Create Account</Button>
        </div>
      </div>
    </Panel>
  );
};

export default LoginForm;
