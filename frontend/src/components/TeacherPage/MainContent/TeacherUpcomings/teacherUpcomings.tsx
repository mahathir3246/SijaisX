
import { Table } from 'rsuite';
import '../../../../scss_stylings/card.module.scss';
import TeacherUpcomingsCardGallery from './Cards/TeacherUpcomingsCardGallery';


const { Column, HeaderCell, Cell } = Table;
import { jobs } from '../../Data/jobsdata';

const TeacherUpcomings = () => {
    return(
        <div>
            <TeacherUpcomingsCardGallery/>
            <Table 
              bordered data={jobs}
              autoHeight
              style={{ marginTop: 20,     /* 10 px space above the table    */
                    minHeight: 280 }}  /* never shrink below 280 px      */>
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

export default TeacherUpcomings;
