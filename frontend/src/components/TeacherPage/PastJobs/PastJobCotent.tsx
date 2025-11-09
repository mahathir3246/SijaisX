import { useState, useEffect } from "react";
import { Panel, Table, Stack, Tag, Badge, Placeholder, Button, Message } from "rsuite";
import EditIcon from "@rsuite/icons/Edit";
import CheckOutlineIcon from "@rsuite/icons/CheckOutline";
import CloseOutlineIcon from "@rsuite/icons/CloseOutline";
import styles from "../../../scss_stylings/PastJob.module.scss";
import { get_completed_batches_for_teacher } from "../../../functions/api_calls";
import AssignmentDetailsModal from "../UpcomingJobs(Teacher)/Cards/CardPopup";





