import { useState , useRef} from 'react';
import {
  Form,type FormInstance, Button, TagPicker, Panel, FlexboxGrid,
  SelectPicker, Uploader, Schema
} from 'rsuite';
import CameraRetroIcon from '@rsuite/icons/legacy/CameraRetro';

import '../Login/Auth.scss';
import Logo from '../../Logo/Logo';
import { schoolsByLocation } from '../data/schoolLists';
import { locations } from '../data/cities';
import { create_teacher, create_substitute } from '../../functions/api_calls';



const roleOptions = [
  {label : "Teacher" , value: "teacher"},
  {label : "Substitute", value: "substitute"}
];

type FormData = {
  role: undefined;
  first_name?: string;
  last_name?: string;
  email?: string;
  phone? : string;
  password?: string;
  confirmPassword?: string;
  location?: string[];
  school?: string[];
  subject?: string[];
  grade?: string[];
  experience?: number;
  profile?: File[];
  picture? : File[];
  highest_education?: string;
}; 
export default function RegisterPage() {
  const [formValue, setFormValue] = useState<FormData>({
  role: undefined,
  first_name: "",
  last_name: "",
  email: "",
  phone: "",
  password: "",
  confirmPassword: "",
  location: [],
  school: [],
  subject: [],
  grade: [],
  experience: 0,
  profile: [],
  picture: [],
  highest_education: ""
});
  const[formError,setFormError] = useState({});
  const formRef = useRef<FormInstance>(null);


  const handleSubmit = async() =>{
    //Run the form’s validation.
    //If the form doesn’t pass (check() is false) or the form isn’t mounted yet (formRef.current is null), 
    // then abort the submit logic right here
    if(!formRef.current?.check()) return;

    const {
      role, first_name, last_name, phone, email,
      password, experience, school,
    } = formValue;

    const name = `${first_name?.trim()} ${last_name?.trim()}`.trim()

    try{
      if(role == "teacher"){
        if(!school || school.length == 0){
          alert("Pick at least one school");
          return;
        }
        const promises = school.map(async (schoolname) => {
          const payload  = {
            name,
            phone_number : phone ?? "",
            school_name: schoolname,
            email: email ?? "",
            password: password ?? ""
          }
          return create_teacher(payload);
        });

      const results = await Promise.allSettled(promises);

      const succeeded = results.filter(r => r.status === "fulfilled").length;
      const failed     = results.filter(r => r.status === "rejected").length;

      alert(`${succeeded} teacher record(s) created${failed ? `, ${failed} failed` : ""}`);

      }else{
        const payloadForSub = {
          name,
          phone_number: phone ?? "",
          email: email ?? "",
          password: password ?? "",
          experience: experience ?? 0,
          highest_education: formValue.highest_education ?? null,
        };

        const subcreate = create_substitute(payloadForSub);
        const results   = await Promise.allSettled([subcreate]); // ← note the [ ]

        const succeeded = results.filter(r => r.status === "fulfilled").length;
        const failed    = results.length - succeeded;

        alert(`${succeeded} substitute record(s) created${failed ? `, ${failed} failed` : ""}`);


        /*
        const grades= formValue.grade ?? [];
        const schools = formValue.school ?? [""];
        const subjects = formValue.subject ?? []; 
        const locations = formValue.location ?? [""];

        const payloadForPref = subjects.flatMap(sub =>
          grades.flatMap(gr =>
            schools.flatMap(sch =>
              locations.map(loc => ({
                grade        : gr,
                substitute_ID: subId,
                school_name  : sch,
                subject      : sub,
                location     : loc
              }))
            )
          )
        );
        */
      }
    }catch(err){
      console.error(err);
      alert("Registration failed – see console for details.");

    }
  }
  const isSubstitute = formValue.role == "substitute";
  const isTeacher = formValue.role == "teacher";

  //Use the selected cities from the form — and if formValue.cities is undefined
  //  (i.e., user hasn’t selected anything), then use an empty array [].
  const selectedCities = formValue.location ?? [];
  const filteredSchools = selectedCities.length
    ? Object.entries(schoolsByLocation)
        .filter(([city]) => selectedCities.includes(city))
        .flatMap(([, schools]) => schools)
    : [];

  
  const validationModel = Schema.Model({
    role: Schema.Types.StringType().isRequired("Choose a role"),
    first_name: Schema.Types.StringType().isRequired("First Name is required"),
    last_name: Schema.Types.StringType().isRequired("Last Name is required"),
    email: Schema.Types.StringType().isEmail("Invalid Email").isRequired("Email is required"),
    phone: Schema.Types.StringType(),
    password: Schema.Types.StringType().isRequired("Password is required"),
    confirmPassword: Schema.Types.StringType()
      .addRule((value, data) => value === data.password, "Passwords do not match")
      .isRequired("Confirm your password"),
    
    ...(isTeacher && {
    location: Schema.Types.ArrayType().addRule((value) => value.length > 0, "At least one location is required"),

    school: Schema.Types.ArrayType()
      .isRequired("Pick the school you work in")
      .addRule((value) => value.length > 0, "At least one school is required"),
    }),

    ...(isSubstitute && {
      /*
      subject: Schema.Types.ArrayType()
        .isRequired("Subject is required")
        .addRule((value) => value.length > 0, "Select at least one subject"),

      grade: Schema.Types.ArrayType()
        .isRequired("Teaching grade is required")
        .addRule((value) => value.length > 0, "Select at least one grade"),
      */
      experience: Schema.Types.NumberType(),
      profile: Schema.Types.ArrayType(),
      picture: Schema.Types.ArrayType(),
      highest_education: Schema.Types.StringType()
      .isRequired('Select your highest education')
      .addRule(
        (value) =>
          ['Peruskoulu','Lukio','Ammattikoulu','Ammattikorkeakoulu','Alempi korkeakoulu','Ylempi korkeakoulu']
            .includes(value),
        'Invalid option'
      ),
    })
  });

  const educationOptions = [
    { label: 'Peruskoulu', value: 'Peruskoulu' },
    { label: 'Lukio', value: 'Lukio' },
    { label: 'Ammattikoulu', value: 'Ammattikoulu' },
    { label: 'Ammattikorkeakoulu', value: 'Ammattikorkeakoulu' },
    { label: 'Alempi korkeakoulu', value: 'Alempi korkeakoulu' },
    { label: 'Ylempi korkeakoulu', value: 'Ylempi korkeakoulu' },
  ];


  return (
    <div className="auth-container">
      <div className="auth-card auth-card--wide">
        <div className="auth-header">
          <div className="auth-logo">
            <Logo size="medium" />
          </div>
          <h1>Create Account</h1>
          <p>Join the modern substitute teaching platform</p>
        </div>
  
        <div className="auth-panel">
          <Form
            fluid
            ref={formRef}
            formValue={formValue}
            onChange={(value) => setFormValue(value as FormData)}
            onCheck={setFormError}
            model={validationModel}
            onSubmit={handleSubmit}
            checkTrigger="blur"
          >
            <Form.Group>
              <Form.ControlLabel>Registering as</Form.ControlLabel>
              <Form.Control
                name="role"
                accepter={SelectPicker}
                data={roleOptions}
                placeholder="Choose…"
                block
              />
            </Form.Group>
  
            <div className="form-row">
              <Form.Group>
                <Form.ControlLabel>First Name</Form.ControlLabel>
                <Form.Control name="first_name" />
              </Form.Group>
  
              <Form.Group>
                <Form.ControlLabel>Last Name</Form.ControlLabel>
                <Form.Control name="last_name" />
              </Form.Group>
            </div>
  
            <Form.Group>
              <Form.ControlLabel>Email</Form.ControlLabel>
              <Form.Control name="email" type="email" placeholder="you@school.fi" />
            </Form.Group>
  
            <Form.Group>
              <Form.ControlLabel>Phone</Form.ControlLabel>
              <Form.Control name="phone" placeholder="+358 40 1234567" />
            </Form.Group>
  
            <div className="form-row">
              <Form.Group>
                <Form.ControlLabel>Password</Form.ControlLabel>
                <Form.Control
                  name="password"
                  type="password"
                  autoComplete="new-password"
                  placeholder="Min. 8 characters"
                />
              </Form.Group>
  
              <Form.Group>
                <Form.ControlLabel>Confirm Password</Form.ControlLabel>
                <Form.Control
                  name="confirmPassword"
                  type="password"
                  autoComplete="new-password"
                  placeholder="Re-enter password"
                />
              </Form.Group>
            </div>
  
            {isTeacher && (
              <>
                <Form.Group>
                  <Form.ControlLabel>Location</Form.ControlLabel>
                  <Form.Control
                    name="location"
                    accepter={TagPicker}
                    data={locations}
                    value={formValue.location}
                    onChange={(vals) => setFormValue({ ...formValue, location: vals })}
                    placeholder="Select the location where the school is situated"
                    block
                  />
                </Form.Group>
  
                <Form.Group>
                  <Form.ControlLabel>School</Form.ControlLabel>
                  <Form.Control
                    accepter={TagPicker}
                    name="school"
                    data={filteredSchools}
                    value={formValue.school}
                    onChange={(selected) => setFormValue({ ...formValue, school: selected })}
                    block
                    disabled={!selectedCities.length}
                    placeholder={
                      selectedCities.length ? 'Select the school you work in' : 'Pick a city first'
                    }
                  />
                </Form.Group>
              </>
            )}
  
            {isSubstitute && (
              <>
                <Form.Group>
                  <Form.ControlLabel>Experience (Years)</Form.ControlLabel>
                  <Form.Control name="experience" type="number" />
                </Form.Group>

                <Form.Group>
                  <Form.ControlLabel>Highest Education</Form.ControlLabel>
                  <Form.Control
                    name="highest_education"
                    accepter={SelectPicker}
                    data={educationOptions}
                    placeholder="Select your highest degree"
                    block
                  />
                </Form.Group>
  
                <Form.Group>
                  <Form.ControlLabel>Profile Picture</Form.ControlLabel>
                  <Uploader multiple listType="picture" action="//jsonplaceholder.typicode.com/posts/">
                    <button>
                      <CameraRetroIcon />
                    </button>
                  </Uploader>
                </Form.Group>
  
                <Form.Group>
                  <Form.ControlLabel>Attach a file (CV, cover letter, etc.)</Form.ControlLabel>
                  <Uploader action="//jsonplaceholder.typicode.com/posts/">
                    <Button>Select files…</Button>
                  </Uploader>
                </Form.Group>
              </>
            )}
  
            <Form.Group>
              <Button
                appearance="primary"
                type="submit"
                block
                disabled={Object.keys(formError).length > 0}
              >
                Create Account
              </Button>
            </Form.Group>
          </Form>
  
          <div className="auth-footer">
            <span>
              Already have an account? <a href="/login">Sign in</a>
            </span>
          </div>
        </div>
      </div>
    </div>
  );
}