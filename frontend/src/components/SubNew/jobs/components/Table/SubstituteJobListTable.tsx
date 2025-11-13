
import "../../TeacherNew/TeacherDashboard.scss"
import { useState,useEffect } from 'react';
import { getUserID } from '../../../../../functions/auth';
import { Header, Button, Table, Panel, Content, Loader } from 'rsuite';
import { get_batch_of_accepted_assignments_for_substitute, get_batch_of_available_assignments_for_substitute, get_all_applied_batches_of_substitute, add_substitute_to_batch } from "../../../../../functions/api_calls";
import SubSidebar from '../../../layout/SubSidebar';
import Logo from '../../../../../Logo/Logo';
import { SubstitutionFE, SubstitutionBE, cardContents } from '../Card/SubstituteJobsCard';
import JobDetails from '../Details/JobDetails';


const { Column, HeaderCell, Cell } = Table;


interface SubUpcomingsProps{
    apiFunction?: (subID:string) => Promise<any>;
}

const statusLabelForView: Record<'available' | 'applied' | 'accepted', 'Available' | 'Applied' | 'Accepted'> = {
    available: 'Available',
    applied: 'Applied',
    accepted: 'Accepted',
  };


const SubstituteJobListTable = ({ apiFunction = get_batch_of_available_assignments_for_substitute }: SubUpcomingsProps) => {

    const view =
    apiFunction === get_batch_of_available_assignments_for_substitute
      ? 'available'
      : apiFunction === get_all_applied_batches_of_substitute
      ? 'applied'
      : 'accepted';

    const statusLabel = statusLabelForView[view];

    const [substitutions, setSubstitutions] = useState<SubstitutionFE[]>([])
    const [originalData, setOriginalData] = useState<SubstitutionBE[]>([])
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);
    const [modalOpen, setModalOpen] = useState(false);
    const [selectedAssignment, setSelectedAssignment] = useState<SubstitutionBE | null>(null);
  
    const [activeKey, setActiveKey] = useState('available-jobs');

    useEffect(() => {
    if (apiFunction === get_batch_of_available_assignments_for_substitute) {
        setActiveKey('available-jobs');
    } else if (apiFunction === get_all_applied_batches_of_substitute) {
        setActiveKey('applied-jobs');
    } else if (apiFunction === get_batch_of_accepted_assignments_for_substitute) {
        setActiveKey('accepted-jobs');
    }
    }, [apiFunction]);
    const [collapsed, setCollapsed] = useState(true);

    const subID = getUserID()

    const fetchAvailableSubs = async () => {
        try{
            if (!subID) {
                setError('No Substitute ID found');
                setLoading(false);
                return;
            }
            
            const response = await apiFunction(subID)

            if (response && response.success){
                let status: 'Applied' | 'Available' | 'Accepted' = 'Available';
                
                if(apiFunction === get_batch_of_available_assignments_for_substitute){
                    status = 'Applied'
                }else if(apiFunction === get_all_applied_batches_of_substitute){
                    status = 'Available'
                }else if(apiFunction === get_batch_of_accepted_assignments_for_substitute){
                    status = 'Accepted'
                }
                const processed = cardContents(response.batches, status);
                setSubstitutions(processed)
                setOriginalData(response.batches)
            }else{
                setError('Failed to fetch Substitutions');
            }
        }catch(error){
            setError(`Error: ${error}`)
        }finally {
            setLoading(false);
        }
    }

    const handleRowClick = (rowData: SubstitutionFE) => {
        const match = originalData.find((assignment) => assignment.batch_ID === rowData.batch_ID);
        if (match) {
          setSelectedAssignment(match);
          setModalOpen(true);
        }
      };

    const handleCloseModal = () => {
    setModalOpen(false);
    setSelectedAssignment(null);
    };
    

    useEffect(()=>{
        fetchAvailableSubs()
    },[apiFunction])

    const handleApply = async (job: SubstitutionFE) => {
        const substituteID = getUserID();
        if (!substituteID) {
          alert('You must be logged in to apply');
          return;
        }
      
        try {
          setLoading(true);
          const result = await add_substitute_to_batch(substituteID, job.batch_ID);
          if (result?.success) {
            alert('Successfully applied!');
            fetchAvailableSubs();
          } else {
            alert(result?.error || 'Failed to apply');
          }
        } catch (err) {
          console.error('Error applying for job:', err);
          alert('An error occurred while applying');
        } finally {
          setLoading(false);
        }
    };
    if (loading) {
        return <Loader size="lg" center />;
    }

    return (
            <div className={`dashboard-container ${collapsed ? 'sidebar-collapsed' : ''}`}>
                <SubSidebar
                    activeKey={activeKey}
                    onSelect={setActiveKey}
                    collapsed={collapsed}
                    onToggle={() => setCollapsed((prev) => !prev)}
                />
                <div className="dashboard-main">
                    <Header className="dashboard-header">
                    <Logo size="small" showText={false} />
                    <div className="header-right">
                        <span className="page-title">My Jobs</span>
                    </div>
                    </Header>

                    <Content className="dashboard-content">
                    
                    <div className="section-header">
                        {apiFunction===get_batch_of_available_assignments_for_substitute &&
                        <>
                        <h3>Available Jobs</h3>
                        <p>Manage and track your Available Jobs</p>
                        </>
                        }
                        {apiFunction===get_all_applied_batches_of_substitute &&
                        <>
                        <h3>Your Applied Jobs</h3>
                        <p>Manage and track your Applied jobs</p>
                        </>
                        }
                        {apiFunction===get_batch_of_accepted_assignments_for_substitute &&
                        <>
                        <h3>Your Accepted Jobs</h3>
                        <p>Manage and track your Accepted jobs</p>
                        </>
                        }
                    </div>

                    <div className="school-jobs-section">
                        {apiFunction===get_batch_of_available_assignments_for_substitute &&
                        <>
                        <h3>All Available job postings</h3>
                        <p className="section-subtitle">
                        Click ‘View Details’ or click the row to see More information about the job.
                        </p>
                        </>
                        }
                        {apiFunction===get_all_applied_batches_of_substitute &&
                        <>
                        <h3>All Applied jobs</h3>
                        <p className="section-subtitle">
                        Click ‘View Details’ or click the row to see More information about the job.
                        </p>
                        </>
                        }
                        {apiFunction===get_batch_of_accepted_assignments_for_substitute &&
                        <>
                        <h3>All Accepted jobs</h3>
                        <p className="section-subtitle">
                        Click ‘View Details’ or click the row to see More information about the job.
                        </p>
                        </>
                        }

                        <Panel bordered>
                        <Table
                            bordered
                            data={substitutions}
                            autoHeight
                            style={{ marginTop: 20, minHeight: 280 }}
                        >
                            <Column flexGrow={2}>
                            <HeaderCell>Date</HeaderCell>
                            <Cell dataKey="date" />
                            </Column>

                            <Column flexGrow={1}>
                            <HeaderCell>From</HeaderCell>
                            <Cell dataKey="beginning_time" />
                            </Column>

                            <Column flexGrow={1}>
                            <HeaderCell>To</HeaderCell>
                            <Cell dataKey="ending_time" />
                            </Column>

                            <Column flexGrow={1}>
                            <HeaderCell>School</HeaderCell>
                            <Cell dataKey="school_name" />
                            </Column>


                            <Column flexGrow={1}>
                            <HeaderCell>Teacher</HeaderCell>
                            <Cell dataKey="teacher_name" />
                            </Column>

                            <Column flexGrow={2}>
                            <HeaderCell>Lessons</HeaderCell>
                            <Cell dataKey="amount_of_hours" />
                            </Column>

                            <Column flexGrow={3}>
                            <HeaderCell>Subject</HeaderCell>
                            <Cell dataKey="subject" />
                            </Column>

                            <Column flexGrow={2}>
                            <HeaderCell>Grades</HeaderCell>
                            <Cell dataKey="grade" />
                            </Column>

                            <Column flexGrow={3}>
                                <HeaderCell>Actions</HeaderCell>
                                <Cell>
                                {(rowData: SubstitutionFE) => (
                                    <div style={{ display: 'flex', gap: 8, justifyContent: 'center' }}>
                                    <Button size="sm" appearance="primary" onClick={() => handleRowClick(rowData)}>
                                        View Details
                                    </Button>

                                    {view === 'available' && (
                                        <Button size="sm" appearance="primary" onClick={() => handleApply(rowData)}>
                                        Apply
                                        </Button>
                                    )}

                                    {view === 'applied' && (
                                        <>
                                        <Button size="sm" appearance="primary" disabled>
                                            Applied ✓
                                        </Button>
                                        <Button
                                            size="sm"
                                            appearance="ghost"
                                            color="red"
                                        >
                                            Withdraw
                                        </Button>
                                        </>
                                    )}

                                    {view === 'accepted' && (
                                        <>
                                        <Button size="sm" appearance="primary" disabled>
                                            Assigned ✓
                                        </Button>
                                        <Button
                                            size="sm"
                                            appearance="ghost"
                                            color="red"
                                        >
                                            Withdraw
                                        </Button>
                                        </>
                                    )}
                                    </div>
                                )}
                                </Cell>
                            </Column>
                        </Table>
                        </Panel>
                    </div>
                    </Content>
                </div>
                <JobDetails
                    open={modalOpen}
                    onClose={handleCloseModal}
                    substitution={selectedAssignment}
                    status={statusLabel}
                />

            </div>
    );
};

export default SubstituteJobListTable;