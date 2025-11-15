import React from 'react';
import sijaisxLogo from "../assets/sijaisx-logo.png";
import './Logo.scss';

interface LogoProps {
  size?: 'small' | 'medium' | 'large';
  showText?: boolean;
  onClick?: () => void;
}

const Logo: React.FC<LogoProps> = ({ size = 'medium', showText = true, onClick  }) => {
  return (
    <div className={`sijais-logo sijais-logo--${size}`} onClick={onClick}>
      <img src={sijaisxLogo} alt="SijaisX Logo" className="sijais-logo__image" />
      
    </div>
  );
};

export default Logo;
