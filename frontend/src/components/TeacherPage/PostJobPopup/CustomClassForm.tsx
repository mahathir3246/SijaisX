import { Button, DateRangePicker } from "rsuite"
import { useState, useEffect } from "react"
import { format } from 'date-fns';
import styles from "../../../scss_stylings/customJobPost.module.scss"
import CustomClassCard from "./CustomCLassCard";
import { CustomJobData } from "./CustomCLassCard";

interface Props{
    onJobsUpdate: (jobs:CustomJobData[]) => void
}

export default function CustomJobs({onJobsUpdate}: Props){
    const [range, setRange] = useState<[Date, Date] | null>(null);
    const [totalClassCount, setTotalClassCount] = useState<number>(0);
    const [dateCards, setDateCards] = useState<{[dateIndex:number]:number[]}>({})
    // Example structure:
    {/*
    0: [0, 1, 2],        // Date index 0 has 3 cards
    1: [0, 1],           // Date index 1 has 2 cards  
    2: [0],              // Date index 2 has 1 card
    3: []                // Date index 3 has 0 cards
    */}
    const[jobData, setJobData]=useState<{[key:string]:CustomJobData}>({})

    const formatDateHeader = (dateString: string) => {
        const date = new Date(dateString)
        return format(date, "dd.MM.yyyy (EEEE)")
    }

    const getDatesInRange = (startDate:Date, endDate:Date) => {
        const dates: Date[] = [];
        const current = new Date(startDate);

        while(current <= endDate){
            dates.push(new Date(current));
            current.setDate(current.getDate() + 1)
        }
        return dates
    }


    //basucally each time a user clicks "add button" it copies all the existing ones into a new one and then 
    //adds one

    const addNewCard = (dateIndex:number) =>{
        setDateCards(prev=>{
            const existingCards = prev[dateIndex] || [];
            const newCardIndex = existingCards.length;
            const key= `${dateIndex}_${newCardIndex}`;
            const date = range ? getDatesInRange(range[0], range[1])[dateIndex] : new Date();
            const dateStr = format(date, 'yyyy-MM-dd');
            setJobData(prevJobData => ({
                ...prevJobData,
                [key]: {
                    subject: '',
                    grade: '',
                    beginning_time: `${dateStr} 00:00`,
                    ending_time: `${dateStr} 00:00`, 
                    room: '',
                    notes: '',
                    date: dateStr

                }
            }));
            
            return {
                ...prev,
                [dateIndex]: [...existingCards, newCardIndex]
            }
        })
    }

    const deleteCard = (dateIndex: number, cardIndex: number) => {
        const cardKey = `${dateIndex}_${cardIndex}`;
        
        setDateCards(prev => ({
            ...prev,
            [dateIndex]: (prev[dateIndex] || []).filter(cardIdx => cardIdx !== cardIndex)
        }));
        
        setJobData(prev => {
            const newData = { ...prev };
            delete newData[cardKey];
            return newData;
        });
    }
    
    const updateJobData = (dateIndex: number, cardIndex: number, updatedData: CustomJobData) => {
        const cardKey = `${dateIndex}_${cardIndex}`;
        setJobData(prev => ({
            ...prev,
            [cardKey]: updatedData
        }));
    };

    const getClassCountForDate=(dateIndex:number)=>{
        return dateCards[dateIndex]?.length || 0;
    }

    useEffect(() => {
        const allJobs: CustomJobData[] = [];
        
        Object.entries(dateCards).forEach(([dateIndexStr, cardIndices]) => {
            const dateIndex = parseInt(dateIndexStr);
            const date = range ? getDatesInRange(range[0], range[1])[dateIndex] : new Date();
            const dateStr = format(date, 'yyyy-MM-dd'); 
            
            cardIndices.forEach(cardIndex => {
                const cardKey = `${dateIndex}_${cardIndex}`;
                const job = jobData[cardKey];
                
                if (job && job.subject.trim() && job.grade.trim()) {
                    allJobs.push({
                        ...job,
                        date: dateStr
                    });
                }
            });
        });
        
        onJobsUpdate(allJobs);
    }, [jobData, dateCards, range, onJobsUpdate]);

    return(
        <div>
            <DateRangePicker
                placeholder="Choose a Date or date Range"
                onChange={value => setRange(value as [Date, Date] | null)}
                value={range}
            />
            <span className={styles.classCount}>Total classes added: {totalClassCount} classes</span>
            
            {range && getDatesInRange(range[0], range[1]).map((date, index) => (  
                <div key={index} className={styles.dayGroup}>
                    <h5>{formatDateHeader(date.toISOString())}</h5>  
                    <span className={styles.classCount}>{getClassCountForDate(index)} classes</span>
                    <Button
                        onClick={() => {
                            addNewCard(index);
                            setTotalClassCount(prev => prev +1);
                        }}
                    >
                        Add Classes
                    </Button>
                    
                    
                    {dateCards[index]?.map((cardIndex) => {
                        const cardKey = `${index}_${cardIndex}`;
                        const currentJobData = jobData[cardKey];
                        
                        if (!currentJobData) return null;
                        
                        return (
                            <div key={cardIndex} style={{ marginTop: '10px', border: '1px solid #ddd', padding: '10px' }}>
                                <CustomClassCard 
                                    jobData={currentJobData}
                                    onUpdate={(updatedData) => updateJobData(index, cardIndex, updatedData)}
                                />
                                <Button
                                    onClick={() => {
                                        deleteCard(index, cardIndex);
                                        setTotalClassCount(prev => prev - 1);
                                    }}
                                    className={styles.cancelButton}
                                >
                                    ❌ Delete Class
                                </Button>
                            </div>
                        );
                    })}
                </div>
            ))}
        </div>
    )
}