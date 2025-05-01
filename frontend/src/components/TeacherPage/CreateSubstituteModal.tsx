import React, { useState } from "react";
import { Modal, Button, DateRangePicker, TimePicker, TagPicker, Input, Checkbox } from "rsuite";

const subjectsList = [
  { label: "Mathematics", value: "Mathematics" },
  { label: "English", value: "English" },
  { label: "Science", value: "Science" },
  { label: "History", value: "History" },
];

const classLevels = [
  { label: "Grade 7", value: "Grade 7" },
  { label: "Grade 8", value: "Grade 8" },
  { label: "Grade 9", value: "Grade 9" },
  { label: "High School", value: "High School" },
];

interface CreateSubstituteModalProps {
  open: boolean;
  onClose: () => void;
}

const CreateSubstituteModal: React.FC<CreateSubstituteModalProps> = ({ open, onClose }) => {
  const [selectedDates, setSelectedDates] = useState<Date[]>([]);
  const [formData, setFormData] = useState<Record<string, any>>({});

  // ✅ Function to handle a RANGE of dates
  const handleDateSelection = (range: [Date, Date]) => {
    if (!range || !range[0] || !range[1]) return; // Ensure valid range
    const [start, end] = range;
  
    let datesArray: Date[] = [];
    let currentDate = new Date(start);
  
    while (currentDate <= end) {
      datesArray.push(new Date(currentDate));
      currentDate.setDate(currentDate.getDate() + 1); // Increment by one day
    }
  
    setSelectedDates(datesArray);
  };
    
  const handleInputChange = (date: string, field: string, value: any) => {
    setFormData((prev) => ({
      ...prev,
      [date]: {
        ...prev[date],
        [field]: value,
      },
    }));
  };

  return (
    <Modal open={open} onClose={onClose} size="lg">
      <Modal.Header>
        <Modal.Title>Luo Sijaisuus</Modal.Title>
      </Modal.Header>

      <Modal.Body>
        <p><strong>Valitse poissaolopäivät :</strong></p>
        <DateRangePicker
          format="yyyy-MM-dd"
          placeholder="Select Date Range"
          onChange={(value, event) => {
            if (value && value[0] && value[1]) {
              handleDateSelection(value); // Pass correct DateRange
            }
          }}
          style={{ width: "100%" }}
        />


        {selectedDates.map((date, index) => (
          <div key={index} style={{ border: "1px solid #ccc", padding: "10px", marginTop: "10px" }}>
            <h5>📅 {new Date(date).toDateString()}</h5>

            <p>⏰ Valitse aikaväli:</p>
            <TimePicker
              format="HH:mm"
              placeholder="Aloitus aika"
              style={{ width: "45%", marginRight: "10px" }}
              onChange={(value) => handleInputChange(date.toISOString(), "timeStart", value)}
            />
            <TimePicker
              format="HH:mm"
              placeholder="Lopetus aika"
              style={{ width: "45%" }}
              onChange={(value) => handleInputChange(date.toISOString(), "timeEnd", value)}
            />

            <p>📚 Valitse aineet:</p>
            <TagPicker
              data={subjectsList}
              placeholder="Aineet"
              style={{ width: "100%" }}
              searchable
              onChange={(value) => handleInputChange(date.toISOString(), "subjects", value)}
            />

            <p>🎓 Valitse luokka-aste:</p>
            <TagPicker
              data={classLevels}
              placeholder="Luokka-asteet"
              style={{ width: "100%" }}
              searchable
              onChange={(value) => handleInputChange(date.toISOString(), "classLevel", value)}
            />

            <p>📝 Tarkemmat ohjeet Sijaiselle:</p>
            <Input
              as="textarea"
              rows={3}
              placeholder="Ohjeet"
              onChange={(value) => handleInputChange(date.toISOString(), "instructions", value)}
            />
          </div>
        ))}

        <div style={{ marginTop: "20px" }}>
          <p>🏫 Koulu:</p>
          <Input placeholder="Koulu" style={{ width: "100%" }} />

          <p>👨‍🏫 Toivottu Sijainen(Valinnainen):</p>
          <Input placeholder="SIjaislista" style={{ width: "100%" }} />

          <p>📩 Vahvistus viesti:</p>
          <Checkbox>Lähetä tekstiviesti kun sijaiset hakevat</Checkbox>
        </div>
      </Modal.Body>

      <Modal.Footer>
        <Button onClick={() => console.log(formData)} appearance="primary">
          Submit
        </Button>
        <Button onClick={onClose} appearance="subtle">
          Cancel
        </Button>
      </Modal.Footer>
    </Modal>
  );
};

export default CreateSubstituteModal;
