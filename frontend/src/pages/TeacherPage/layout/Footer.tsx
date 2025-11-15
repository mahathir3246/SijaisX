import { FiMail, FiPhone, FiMapPin } from 'react-icons/fi';
import { FaFacebook, FaInstagram, FaXTwitter, FaLinkedin } from 'react-icons/fa6';
import Logo from '../../../Logo/Logo';
import "../TeacherDashboard.scss"

const TeacherFooter: React.FC = () => {
  const currentYear = new Date().getFullYear();

  return (
    <footer className="dashboard-footer">
      <div className="footer-content">
        <div className="footer-section footer-brand">
          <Logo size="small" />
          <p>Connecting teachers with qualified substitutes across Finland</p>
          <div className="social-links">
            <a href="https://facebook.com" target="_blank" rel="noopener noreferrer" aria-label="Facebook">
              <FaFacebook />
            </a>
            <a href="https://instagram.com" target="_blank" rel="noopener noreferrer" aria-label="Instagram">
              <FaInstagram />
            </a>
            <a href="https://twitter.com" target="_blank" rel="noopener noreferrer" aria-label="X (Twitter)">
              <FaXTwitter />
            </a>
            <a href="https://linkedin.com" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn">
              <FaLinkedin />
            </a>
          </div>
        </div>

        <div className="footer-section">
          <h4>Quick Links</h4>
          <ul>
            <li><a href="/help">Help Center</a></li>
            <li><a href="/about">About Us</a></li>
            <li><a href="/terms">Terms of Service</a></li>
            <li><a href="/privacy">Privacy Policy</a></li>
          </ul>
        </div>

        <div className="footer-section">
          <h4>Contact</h4>
          <ul className="contact-list">
            <li>
              <FiMail />
              <a href="mailto:support@sijaisx.fi">support@sijaisx.fi</a>
            </li>
            <li>
              <FiPhone />
              <a href="tel:+358401234567">+358 40 123 4567</a>
            </li>
            <li>
              <FiMapPin />
              <span>Helsinki, Finland</span>
            </li>
          </ul>
        </div>
      </div>

      <div className="footer-bottom">
        <p>&copy; {currentYear} SijaisX. All rights reserved.</p>
      </div>
    </footer>
  );
};

export default TeacherFooter;
