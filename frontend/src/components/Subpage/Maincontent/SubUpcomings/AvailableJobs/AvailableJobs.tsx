import { Table } from "rsuite";
import { useEffect, useState } from "react";
import { get_all_assignments_available_to_sub } from "../../../../../functions/api_calls";
import { getUserID } from "../../../../../functions/auth";


const { Column, HeaderCell, Cell } = Table;

export interface AvailabeAssignments{
    assignment_ID: string;
    beginning_time: string,
    date: string,
    ending_time: string,
    grade: string,
    notes: string,
    room: string,
    school_name: string,
    status: string,
    subject: string,
    teacher_name: string
}

export interface JobCard{
    date: string,
    beginning_time: string,
    ending_time: string,
    grade: string,
    school_name: string,
    subject: string,
    teacher_name: string
}

export function tableAndCardContents(assignments:AvailabeAssignments[]): JobCard[] {
    return assignments.map(assgnment =>{
        
    })

}