import '../../../../scss_stylings/card.module.scss';
import { useState, useEffect } from 'react';
import { getUserID } from '../../../../functions/auth';
import SubUpcomingsCardGallery from './Cards/SubUpcomingsCardGallery';
import { Loader } from 'rsuite';
import { SubstitutionFE } from './subUpcomings';

const SubApplied = () => {
    const [appliedJobs, setAppliedJobs] = useState<SubstitutionFE[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    const subID = getUserID();

    useEffect(() => {
        // For now, just show empty state
        // We'll add API call later
        setLoading(false);
        setAppliedJobs([]);
    }, []);

    if (loading) {
        return <Loader size="lg" center />;
    }

    if (appliedJobs.length === 0) {
        return (
            <div style={{ textAlign: 'center', padding: '20px', color: '#666' }}>
                No applied jobs yet
            </div>
        );
    }

    return (
        <div>
            <SubUpcomingsCardGallery substitutions={appliedJobs} />
        </div>
    );
};

export default SubApplied;