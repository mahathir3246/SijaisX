import React from 'react';
import sijaisxLogo from "../assets/sijaisx-logo.png";
import './Logo.scss';

interface LogoProps {
  size?: 'small' | 'medium' | 'large';
  showText?: boolean;
}

const Logo: React.FC<LogoProps> = ({ size = 'medium', showText = true }) => {
  return (
    <div className={`sijais-logo sijais-logo--${size}`}>
      <img src={sijaisxLogo} alt="SijaisX Logo" className="sijais-logo__image" />
    </div>
  );
};

export default Logo;
