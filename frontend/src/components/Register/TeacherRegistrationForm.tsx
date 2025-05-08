import { useState, useMemo } from 'react';
import {
  Form, Button, TagPicker, RadioGroup, Radio,
  Panel, FlexboxGrid, Divider, Message, Schema
} from 'rsuite';
import { createUserWithEmailAndPassword, getAuth } from 'firebase/auth';
import { useNavigate } from 'react-router-dom';
import { addDataToFirestore } from '../../../firestore';
import styles from '../../scss_stylings/teacher_register.module.scss';
import {
  schoolsByCity,
} from '../data/schoolLists';
import { CityValue,cityOptions } from '../data/cities';
import { subjectOptions, luokkasteOptions } from '../data/options';


const { StringType, ArrayType } = Schema.Types;

const model = Schema.Model({
  name:            StringType().isRequired(),
  email:           StringType().isEmail().isRequired(),
  cities:          ArrayType().minLength(1, 'Pick at least one city'),
  gender:          StringType().isRequired('Pick gender'),
  schools:         ArrayType().minLength(1, 'Pick at least one school'),
  subjects:        ArrayType().minLength(1, 'Pick at least one subject'),
  luokkaste:       ArrayType().minLength(1),
  phone:           StringType()
                    .pattern(/^\+?\d{7,15}$/, 'Enter a valid phone')
                    .isRequired('Phone number is required'),
  password:        StringType().minLength(6).isRequired(),
  confirmPassword: StringType(),
  bio:             StringType()
});

/* ---------- component ---------- */
export default function TeacherRegistrationForm() {
  const navigate                      = useNavigate();

  /* form state */
  const [formValue, setFormValue]     = useState<Record<string, any>>({});
  const [loading, setLoading]         = useState(false);
  const [errorMsg, setErrorMsg]       = useState('');

  /* city & school helper state */
  const cities   = (formValue.cities ?? []) as CityValue[];
  const schools  = formValue.schools ?? [];

  /** All schools from *any* selected city (deduped) */
  const schoolChoices = useMemo(() => {
    const merged = cities.flatMap(c => schoolsByCity[c] ?? []);
    // dedupe by value
    const map = new Map<string, { label: string; value: string }>();
    merged.forEach(s => map.set(s.value, s));
    return [...map.values()];
  }, [cities]);

  /* ---------- handlers ---------- */

  /* removing invalid schools if city set shrinks */
  const handleCityChange = (vals: CityValue[]) => {
    const allowed = new Set(
      vals.flatMap(c => schoolsByCity[c].map(s => s.value))
    );
    const filteredSchools = schools.filter((s: string) => allowed.has(s));

    setFormValue({
      ...formValue,
      cities: vals,
      schools: filteredSchools         // keep only still‑valid schools
    });
  };

  const handleSubmit = async (ok: boolean) => {
    if (!ok) return;

    const {
      name, email,phone, password, confirmPassword,
      cities, gender, schools,
      subjects, luokkaste, bio
    } = formValue;

    if (password !== confirmPassword) {
      setErrorMsg('Passwords do not match');
      return;
    }

    try {
      setLoading(true);

      const cred = await createUserWithEmailAndPassword(getAuth(), email, password);

      await addDataToFirestore('teachers', {
        name,
        email,
        phone,
        cities,
        gender,
        schools,
        subjects,
        luokkaste,
        bio,
        uid: cred.user.uid
      });

      navigate('/');
    } catch (e: any) {
      setErrorMsg(e.message ?? 'Something went wrong');
    } finally {
      setLoading(false);
    }
  };

  /* ---------- UI ---------- */
  return (
    <div className={styles.pageBg}>
      <FlexboxGrid justify="center" className={styles.teacherRegisterWrapper}>
        <FlexboxGrid.Item colspan={24}>
          <Panel bordered shaded className={styles.registerPanel} header="Teacher Registration">
            {errorMsg && <Message type="error" showIcon>{errorMsg}</Message>}

            <Form
              fluid
              model={model}
              formValue={formValue}
              onChange={setFormValue}
              onSubmit={formErr => handleSubmit(!formErr)}
              checkTrigger="blur"
            >
              <Form.Group controlId="name">
                <Form.ControlLabel>Name</Form.ControlLabel>
                <Form.Control name="name" />
              </Form.Group>

              <Form.Group controlId="gender">
                <Form.ControlLabel>Gender</Form.ControlLabel>
                <RadioGroup
                  name="gender"
                  inline
                  value={formValue.gender}
                  onChange={val => setFormValue({ ...formValue, gender: val })}
                >
                  <Radio value="male">Male</Radio>
                  <Radio value="female">Female</Radio>
                  <Radio value="other">Other</Radio>
                </RadioGroup>
              </Form.Group>

              <Form.Group controlId="email">
                <Form.ControlLabel>Email</Form.ControlLabel>
                <Form.Control name="email" type="email" />
              </Form.Group>

              <Form.Group controlId="phone">
                <Form.ControlLabel>Phone Number</Form.ControlLabel>
                <Form.Control 
                  name="phone" 
                  placeholder="+358 40 1234567" 
                  style={{ width: '100%' }} 
                />
              </Form.Group>

              <Divider />

              {/* ------------ city picker (multi) ------------ */}
              <Form.Group controlId="cities">
                <Form.ControlLabel>City / Cities</Form.ControlLabel>
                <TagPicker
                  name="cities"
                  data={[...cityOptions]}      // spread removes readonly
                  value={cities}
                  onChange={(vals) => handleCityChange(vals as CityValue[])}
                  placeholder="Select city / cities"
                  block
                />
              </Form.Group>

              {/* ------------ schools (depends on city) ------------ */}
              <Form.Group controlId="schools">
                <Form.ControlLabel>School(s)</Form.ControlLabel>
                <TagPicker
                  name="schools"
                  data={schoolChoices}
                  value={schools}
                  onChange={val => setFormValue({ ...formValue, schools: val })}
                  disabled={cities.length === 0}
                  placeholder={cities.length ? 'Select school(s)' : 'Pick city first'}
                  block
                />
              </Form.Group>

              <Form.Group controlId="subjects">
                <Form.ControlLabel>Subject(s)</Form.ControlLabel>
                <TagPicker name="subjects" data={subjectOptions} block />
              </Form.Group>

              <Form.Group controlId="luokkaste">
                <Form.ControlLabel>Teaching Level (Luokkaste)</Form.ControlLabel>
                <TagPicker name="luokkaste" data={luokkasteOptions} block />
              </Form.Group>


              <Form.Group controlId="bio">
                <Form.ControlLabel>Short Bio / Additional Info </Form.ControlLabel>
                <Form.Control
                  accepter="textarea"
                  name="bio"    
                  rows={4}
                  defaultValue="Tell us a little about yourself..."
                  style={{ resize: 'vertical' }}
                  className={styles.box}
                />
              </Form.Group>
              
              <Divider> Security </Divider>

              <Form.Group controlId="password">
                <Form.ControlLabel>Password</Form.ControlLabel>
                <Form.Control name="password" type="password" autoComplete="new-password" />
              </Form.Group>

              <Form.Group controlId="confirmPassword">
                <Form.ControlLabel>Confirm Password</Form.ControlLabel>
                <Form.Control name="confirmPassword" type="password" autoComplete="new-password" />
              </Form.Group>

              <Form.Group>
                <Button appearance="primary" type="submit" loading={loading} block>
                  Register
                </Button>
              </Form.Group>
            </Form>
          </Panel>
        </FlexboxGrid.Item>
      </FlexboxGrid>
    </div>
  );
}
