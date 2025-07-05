
import { Table } from 'rsuite';
import '../../../scss_stylings/teacher.module.scss';

const { Column, HeaderCell, Cell } = Table;

type JobInSchool = {
  subfor: string;
  class: string;
  subject: string;
  date:string;
  status: 'Pending' | 'Searching' | 'Accepted' | 'Revoked'
};

const jobs: JobInSchool[] = [
  {subfor: "Riikka Ruusuvuori", class :"7C", subject: "Biology", date:"27.01.2025 8.15-9.00", status: "Pending"},
  {subfor: "Noora Jokiniemi",class :"8B", subject: "Chemistry", date:"27.01.2025 9.00-9.45", status: "Searching"},
  {subfor: "Abdi Rahman",class :"9A", subject: "Physics", date:"27.01.2025 10.15-11.00", status: "Accepted"},
  {subfor: "Irfan Hossain",class :"9C", subject: "Math", date:"27.02.20251 11.00-11.45", status: "Revoked"},
];

const SchoolUpcomings = () => {
    return(
        <div>
            <Table 
              bordered data={jobs}
              autoHeight
              style={{ minHeight: 280 }}>

                <Column flexGrow={2}>
                    <HeaderCell>Substitute for</HeaderCell>
                    <Cell dataKey="subfor"/>               
                </Column>


                <Column flexGrow={1}>
                    <HeaderCell>Class</HeaderCell>
                    <Cell dataKey="class"/>               
                </Column>

                <Column flexGrow={1}>
                    <HeaderCell>Subject</HeaderCell>
                    <Cell dataKey="subject" />
                </Column>

                <Column flexGrow={2}>
                    <HeaderCell>Date</HeaderCell>
                    <Cell dataKey='date'/>
                </Column>

                <Column flexGrow={1}>
                    <HeaderCell>Status</HeaderCell>
                    <Cell dataKey='status'/>
                </Column>

            </Table>
        </div>
    )
};

export default SchoolUpcomings;
