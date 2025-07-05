import { Panel, Form, Button, Input, Divider } from 'rsuite';
import styles from '../../scss_stylings/login.module.scss';

const LoginForm = () => {
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

        <Form fluid>
          <Form.Group>
            <Form.ControlLabel>Email Address</Form.ControlLabel>
            <Form.Control
              name="email"
              type="email"
              accepter={Input}
              placeholder="Enter your email"
            />
          </Form.Group>

          <Form.Group>
            <Form.ControlLabel>Password</Form.ControlLabel>
            <Form.Control
              name="password"
              type="password"
              accepter={Input}
              placeholder="Enter your password"
            />
          </Form.Group>

          <Form.Group>
            <Button appearance="primary" size="lg" block>
              Sign In
            </Button>
          </Form.Group>
        </Form>

        <Divider>or</Divider>

        <div className={styles.authSwitch}>
          <p>Don’t have an account?</p>
          <Button appearance="link">Create Account</Button>
        </div>
      </div>
    </Panel>
  );
};

export default LoginForm;
