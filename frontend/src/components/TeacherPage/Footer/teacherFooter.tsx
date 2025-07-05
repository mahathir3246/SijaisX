"use client";
import { Link } from 'react-router-dom';
import footerStyles from "../../../scss_stylings/footer.module.scss";

const Footer = () => {
  const currentYear = new Date().getFullYear();
  return (
    <>
      <div className={footerStyles.footerDiv}>
        <div className={footerStyles.footerDivLogoAndText}>
          <Link className={footerStyles.logoContainerFooter} to="/">
            <div className={footerStyles.footerlogoBig}>
              SijaisX
            </div>
          </Link>
          <div className={footerStyles.textContainerFooter}>
            <div className={footerStyles.textContainerItem}>
              <p className={footerStyles.footerBottomSublistTitle}>
                Tietoa Meistä
              </p>
              <Link className={footerStyles.footerBottomSublistItem} to="/">
              Tavoitteemme
              </Link>
              <Link className={footerStyles.footerBottomSublistItem} to="/">
                Ura
              </Link>
            </div>
            <div className={footerStyles.textContainerItem}>
              <p className={footerStyles.footerBottomSublistTitle}>
              Palvelut
              </p>
              <Link
                className={footerStyles.footerBottomSublistItem}
                to="/"
                target="_blank"
                rel="noopener noreferrer"
              >
                Yhetistyökoulut
              </Link>
              <Link
                className={footerStyles.footerBottomSublistItem}
                to="/"
                target="_blank"
                rel="noopener noreferrer"
              >
                Sijaisille
              </Link>
              <Link
                className={footerStyles.footerBottomSublistItem}
                to="/"
                target="_blank"
                rel="noopener noreferrer"
              >
                Opettajille
              </Link>
            </div>
            <div className={footerStyles.textContainerItem}>
              <p className={footerStyles.footerBottomSublistTitle}>
              Yhteystiedot
              </p>
              <Link
                className={footerStyles.footerBottomSublistItem}
                to="/"
                target="_blank"
                rel="noopener noreferrer"
              >
                Ota yhteyttä
              </Link>
              <Link
                className={footerStyles.footerBottomSublistItem}
                to="/"
                target="_blank"
                rel="noopener noreferrer"
              >
                UKK (Usein kysytyt kysymykset)
              </Link>
              <Link
                className={footerStyles.footerBottomSublistItem}
                to="/"
                target="_blank"
                rel="noopener noreferrer"
              >
                Tietosuojakäytäntö
              </Link>
            </div>
          </div>
        </div>
      </div>
      <div className={footerStyles.footerDivCopyright}>
        <div className={footerStyles.footerDivSubContainer}>
          <p className={footerStyles.copyrightText}>
            © {currentYear} SijaisX. All Rights Reserved.
          </p>
        </div>
      </div>
    </>
  );
};

export default Footer;
