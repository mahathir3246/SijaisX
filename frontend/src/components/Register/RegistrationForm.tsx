import { useState , useRef} from 'react';
import {
  Form,type FormInstance, Button, TagPicker, Panel, FlexboxGrid,
  SelectPicker, Uploader, Schema
} from 'rsuite';
import CameraRetroIcon from '@rsuite/icons/legacy/CameraRetro';

import styles from '../../scss_stylings/register.module.scss';
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
}; 
export default function RegistrationForm() {
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
  picture: []
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
          experience: experience ?? 0
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
      picture: Schema.Types.ArrayType()
    })
  });


  return (
    <div className={styles.pageBg}>
      <FlexboxGrid justify="center" className={styles.teacherRegisterWrapper}>
        <FlexboxGrid.Item colspan={24}>
          <Panel bordered shaded className={styles.registerPanel} header="Registration Form">

            <Form
              fluid
              ref={formRef} 
              onSubmit={handleSubmit}
              formValue={formValue}
              onChange={(value) => setFormValue(value as FormData)}
              onCheck={setFormError}
              model={validationModel}
              checkTrigger="blur"
            >
              {/* Select role */}
              <Form.Group>
                <Form.ControlLabel>Registering as</Form.ControlLabel>

                <Form.Control
                  name="role"                       // must match schema key
                  accepter={SelectPicker}           // tell RSuite which widget to render
                  data={roleOptions}
                  placeholder="Choose…"             // shows “Choose…” when empty
                  block
                />
              </Form.Group>

              {/* Common fields */}
              <Form.Group>
                <Form.ControlLabel>First Name</Form.ControlLabel>
                <Form.Control name="first_name" />
              </Form.Group>

              <Form.Group>
                <Form.ControlLabel>Last Name</Form.ControlLabel>
                <Form.Control name="last_name" />
              </Form.Group>

              <Form.Group>
                <Form.ControlLabel>Email</Form.ControlLabel>
                <Form.Control name="email" type="email" placeholder='youremail@example.com' />
              </Form.Group>

              <Form.Group>
                <Form.ControlLabel>Phone</Form.ControlLabel>
                <Form.Control name="phone" placeholder="+358 40 1234567" />
              </Form.Group>

              <Form.Group>
                <Form.ControlLabel>Password</Form.ControlLabel>
                <Form.Control name="password" type="password" autoComplete="new-password" placeholder='********'/>
              </Form.Group>

              <Form.Group>
                <Form.ControlLabel>Confirm Password</Form.ControlLabel>
                <Form.Control name="confirmPassword" type="password" autoComplete="new-password" placeholder='********'/>
              </Form.Group>
              {isTeacher && (
                <>
                <Form.Group>
                  <Form.ControlLabel>Location</Form.ControlLabel>
                  <Form.Control
                    name="location"                         // it must match the schema key
                    accepter={TagPicker}                    // tell Form which component to render
                    data={locations}
                    value={formValue.location}
                    onChange={(vals) => {
                      setFormValue({ ...formValue, location: vals });
                    }}
                    placeholder="Selct the location where the school is situated"
                    block
                  />
                </Form.Group>

                <Form.Group>
                  <Form.ControlLabel>School</Form.ControlLabel>
                  <Form.Control
                    accepter={TagPicker}
                    name = "school"
                    data = {filteredSchools}
                    value = {formValue.school}
                    onChange={(selected) => setFormValue({ ...formValue, school: selected })}
                    block
                    disabled={!selectedCities.length}
                    placeholder = "Pick a city"
                  />
                </Form.Group>
                </>
              )}
              {/*Substitute-only fields */}
              {isSubstitute && (
                <>
                  {/*
                  <Form.Group>
                    <Form.ControlLabel>Subject(s)</Form.ControlLabel>
                    <Form.Control
                      accepter={TagPicker}
                      name="subject" 
                      data={subjectOptions}
                      value={formValue.subject}
                      onChange={(selected) => setFormValue({ ...formValue, subject: selected })} 
                      block
                      placeholder = "Pick the subject(s) you teach"
                    />
                  </Form.Group>

                  <Form.Group>
                    <Form.ControlLabel>Grade(s)</Form.ControlLabel>
                    <Form.Control
                      accepter={TagPicker}
                      name="grade" 
                      data={luokkasteOptions}
                      value={formValue.grade}
                      onChange={(selected) => setFormValue({ ...formValue, grade: selected })} 
                      block
                      placeholder = "Pick the grade you teach in"
                    />
                  </Form.Group>

                  

                  */}
                  

                  <Form.Group>
                    <Form.ControlLabel>Experience (Years)</Form.ControlLabel>
                    <Form.Control name="experience" type="number" />
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
                    <Form.ControlLabel>Attach a file(CV, cover letter etc..)</Form.ControlLabel>
                    <Uploader action="//jsonplaceholder.typicode.com/posts/">
                      <Button>Select files...</Button>
                    </Uploader>
                  </Form.Group>
                </>
              )}

              {/* Submit */}
              <Form.Group>
                <Button
                  appearance="primary"
                  type="submit"
                  block
                  disabled={Object.keys(formError).length > 0}
                >
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