import { useState, useEffect, useRef } from 'react';
import { Modal, Button, DateRangePicker, Form, Grid, Row, Col } from 'rsuite';
import type { FormInstance } from 'rsuite';
import { format } from 'date-fns';
import { lessonsBydate, Assignment } from './Data/jobsdata';


interface Props { open: boolean; onClose(): void; }

export default function PostJobModal({ open, onClose }: Props) {
  const [range, setRange] = useState<[Date, Date] | null>(null);
  const [selectedLessons, setSelectedLessons] = useState<Assignment[]>([]);


  // 1. whenever dates change, re-hydrate form rows from mock file
  useEffect(() => {
    if (!range) return;

    const [from, to] = range;
    const days: Assignment[] = [];

    for (
      let d = new Date(from);
      d <= to;
      d.setDate(d.getDate() + 1)
    ) {
      const key = format(d, 'yyyy-MM-dd') as keyof typeof lessonsBydate;
      const lessons = lessonsBydate[key] ?? [];
      days.push(...lessons);
    }
    setSelectedLessons(days);
  }, [range]);

  // 2. user may also edit / add rows manually in the form
  const onChangeLesson = (index: number, patch: Partial<Assignment>) => {
    setSelectedLessons(prev => {
      const next = [...prev];
      next[index] = { ...next[index], ...patch };
      return next;
    });
  };

  const formRef = useRef<FormInstance<Record<string, any>>>(null);

  return (
    <Modal size="lg" open={open} onClose={onClose}>
      <Modal.Header><h4>Post a Job</h4></Modal.Header>

      <Modal.Body>
        <DateRangePicker
          style={{ width: '100%' }}
          onChange={(value) => setRange(value as [Date, Date] | null)}
          placeholder="Choose date or date range"
        />

        <Form
          fluid
          ref={formRef}
          formDefaultValue={{ lessons: selectedLessons }}   // initial fill
          className="mt-4"
        >
          {selectedLessons.map((l, idx) => (
            <Grid key={idx} className="mb-3">
              <Row gutter={8}>
                <Col xs={5}>
                  <Form.Control name={`lessons-${idx}-subject`} defaultValue={l.subject} />
                </Col>
                <Col xs={3}>
                  <Form.Control name={`lessons-${idx}-grade`}   defaultValue={l.grade} />
                </Col>
                <Col xs={3}>
                  <Form.Control name={`lessons-${idx}-start`}   defaultValue={l.start} />
                </Col>
                <Col xs={3}>
                  <Form.Control name={`lessons-${idx}-end`}     defaultValue={l.end} />
                </Col>
                <Col xs={3}>
                  <Form.Control name={`lessons-${idx}-room`}    defaultValue={l.room} />
                </Col>
                <Col xs={5}>
                  <Form.Control name={`lessons-${idx}-school`}  defaultValue={l.school} />
                </Col>
              </Row>
            </Grid>
          ))}
        </Form>
      </Modal.Body>

      <Modal.Footer>
        <Button  appearance="primary">Submit</Button>
        <Button onClick={onClose} appearance="subtle">Cancel</Button>
      </Modal.Footer>
    </Modal>
  );
}
