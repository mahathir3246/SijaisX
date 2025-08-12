import { Table } from "rsuite";
import { useEffect, useState } from "react";
import { get_all_assignments_available_to_sub } from "../../../../../functions/api_calls";
import { getUserID } from "../../../../../functions/auth";


const { Column, HeaderCell, Cell } = Table;

export assignment