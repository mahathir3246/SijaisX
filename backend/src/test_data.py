# test_data.py
from .db import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()

try:
    cursor.executescript("""
    INSERT INTO School Values('sc_joni','Jokiniemen Koulu');
    INSERT INTO Teacher Values('t_mikavanhamki_joni','Mika Vanhamäki','+3584125499', 'mika.vanhamaki@eduvantaa.fi', '1234', 'sc_joni' );
    INSERT INTO Substitute VALUES('sub_granitzogjani', 'Granit Zogjani', '+358401234567', 'granit.zogjani@email.com', '123', 5, 'Ammattikorkeakoulu', NULL, NULL);
    INSERT INTO VolunteersInSchool VALUES('sub_granitzogjani', 'sc_joni'); 
    INSERT INTO Class VALUES("cl_ma_7a_202511100815_202511100900_dur_45_rm_a101", "Mathematics", "7A", "2025-11-10 08:15", "2025-11-10 09:00", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202511100815_202511100900_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ch_8b_202511100900_202511100945_dur_45_rm_b204", "Chemistry", "8B", "2025-11-10 09:00", "2025-11-10 09:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202511100900_202511100945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ma_7b_202511101000_202511101045_dur_45_rm_a102", "Mathematics", "7B", "2025-11-10 10:00", "2025-11-10 10:45", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202511101000_202511101045_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_9a_202511101100_202511101145_dur_45_rm_b205", "Chemistry", "9A", "2025-11-10 11:00", "2025-11-10 11:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202511101100_202511101145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ma_8c_202511101230_202511101315_dur_45_rm_a103", "Math", "8C", "2025-11-10 12:30", "2025-11-10 13:15", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202511101230_202511101315_dur_45_rm_a103");

    INSERT INTO Class VALUES("cl_ma_7a_202511170815_202511170900_dur_45_rm_a101", "Mathematics", "7A", "2025-11-17 08:15", "2025-11-17 09:00", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202511170815_202511170900_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ch_8b_202511170900_202511170945_dur_45_rm_b204", "Chemistry", "8B", "2025-11-17 09:00", "2025-11-17 09:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202511170900_202511170945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ma_7b_202511171000_202511171045_dur_45_rm_a102", "Mathematics", "7B", "2025-11-17 10:00", "2025-11-17 10:45", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202511171000_202511171045_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_9a_202511171100_202511171145_dur_45_rm_b205", "Chemistry", "9A", "2025-11-17 11:00", "2025-11-17 11:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202511171100_202511171145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ma_8c_202511171230_202511171315_dur_45_rm_a103", "Math", "8C", "2025-11-17 12:30", "2025-11-17 13:15", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202511171230_202511171315_dur_45_rm_a103");

    INSERT INTO Class VALUES("cl_ma_7a_202511240815_202511240900_dur_45_rm_a101", "Mathematics", "7A", "2025-11-24 08:15", "2025-11-24 09:00", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202511240815_202511240900_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ch_8b_202511240900_202511240945_dur_45_rm_b204", "Chemistry", "8B", "2025-11-24 09:00", "2025-11-24 09:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202511240900_202511240945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ma_7b_202511241000_202511241045_dur_45_rm_a102", "Mathematics", "7B", "2025-11-24 10:00", "2025-11-24 10:45", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202511241000_202511241045_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_9a_202511241100_202511241145_dur_45_rm_b205", "Chemistry", "9A", "2025-11-24 11:00", "2025-11-24 11:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202511241100_202511241145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ma_8c_202511241230_202511241315_dur_45_rm_a103", "Math", "8C", "2025-11-24 12:30", "2025-11-24 13:15", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202511241230_202511241315_dur_45_rm_a103");

    INSERT INTO Class VALUES("cl_ma_7a_202512010815_202512010900_dur_45_rm_a101", "Mathematics", "7A", "2025-12-01 08:15", "2025-12-01 09:00", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202512010815_202512010900_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ch_8b_202512010900_202512010945_dur_45_rm_b204", "Chemistry", "8B", "2025-12-01 09:00", "2025-12-01 09:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202512010900_202512010945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ma_7b_202512011000_202512011045_dur_45_rm_a102", "Mathematics", "7B", "2025-12-01 10:00", "2025-12-01 10:45", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202512011000_202512011045_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_9a_202512011100_202512011145_dur_45_rm_b205", "Chemistry", "9A", "2025-12-01 11:00", "2025-12-01 11:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202512011100_202512011145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ma_8c_202512011230_202512011315_dur_45_rm_a103", "Math", "8C", "2025-12-01 12:30", "2025-12-01 13:15", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202512011230_202512011315_dur_45_rm_a103");

    INSERT INTO Class VALUES("cl_ma_7a_202512080815_202512080900_dur_45_rm_a101", "Mathematics", "7A", "2025-12-08 08:15", "2025-12-08 09:00", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202512080815_202512080900_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ch_8b_202512080900_202512080945_dur_45_rm_b204", "Chemistry", "8B", "2025-12-08 09:00", "2025-12-08 09:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202512080900_202512080945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ma_7b_202512081000_202512081045_dur_45_rm_a102", "Mathematics", "7B", "2025-12-08 10:00", "2025-12-08 10:45", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202512081000_202512081045_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_9a_202512081100_202512081145_dur_45_rm_b205", "Chemistry", "9A", "2025-12-08 11:00", "2025-12-08 11:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202512081100_202512081145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ma_8c_202512081230_202512081315_dur_45_rm_a103", "Math", "8C", "2025-12-08 12:30", "2025-12-08 13:15", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202512081230_202512081315_dur_45_rm_a103");

    INSERT INTO Class VALUES("cl_ma_7a_202512150815_202512150900_dur_45_rm_a101", "Mathematics", "7A", "2025-12-15 08:15", "2025-12-15 09:00", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202512150815_202512150900_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ch_8b_202512150900_202512150945_dur_45_rm_b204", "Chemistry", "8B", "2025-12-15 09:00", "2025-12-15 09:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202512150900_202512150945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ma_7b_202512151000_202512151045_dur_45_rm_a102", "Mathematics", "7B", "2025-12-15 10:00", "2025-12-15 10:45", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202512151000_202512151045_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_9a_202512151100_202512151145_dur_45_rm_b205", "Chemistry", "9A", "2025-12-15 11:00", "2025-12-15 11:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202512151100_202512151145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ma_8c_202512151230_202512151315_dur_45_rm_a103", "Math", "8C", "2025-12-15 12:30", "2025-12-15 13:15", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202512151230_202512151315_dur_45_rm_a103");

    INSERT INTO Class VALUES("cl_ma_7a_202512220815_202512220900_dur_45_rm_a101", "Mathematics", "7A", "2025-12-22 08:15", "2025-12-22 09:00", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202512220815_202512220900_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ch_8b_202512220900_202512220945_dur_45_rm_b204", "Chemistry", "8B", "2025-12-22 09:00", "2025-12-22 09:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202512220900_202512220945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ma_7b_202512221000_202512221045_dur_45_rm_a102", "Mathematics", "7B", "2025-12-22 10:00", "2025-12-22 10:45", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202512221000_202512221045_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_9a_202512221100_202512221145_dur_45_rm_b205", "Chemistry", "9A", "2025-12-22 11:00", "2025-12-22 11:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202512221100_202512221145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ma_8c_202512221230_202512221315_dur_45_rm_a103", "Math", "8C", "2025-12-22 12:30", "2025-12-22 13:15", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202512221230_202512221315_dur_45_rm_a103");

    INSERT INTO Class VALUES("cl_ma_7a_202512290815_202512290900_dur_45_rm_a101", "Mathematics", "7A", "2025-12-29 08:15", "2025-12-29 09:00", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202512290815_202512290900_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ch_8b_202512290900_202512290945_dur_45_rm_b204", "Chemistry", "8B", "2025-12-29 09:00", "2025-12-29 09:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202512290900_202512290945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ma_7b_202512291000_202512291045_dur_45_rm_a102", "Mathematics", "7B", "2025-12-29 10:00", "2025-12-29 10:45", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202512291000_202512291045_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_9a_202512291100_202512291145_dur_45_rm_b205", "Chemistry", "9A", "2025-12-29 11:00", "2025-12-29 11:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202512291100_202512291145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ma_8c_202512291230_202512291315_dur_45_rm_a103", "Math", "8C", "2025-12-29 12:30", "2025-12-29 13:15", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202512291230_202512291315_dur_45_rm_a103");

    INSERT INTO Class VALUES("cl_ma_7a_202601050815_202601050900_dur_45_rm_a101", "Mathematics", "7A", "2026-01-05 08:15", "2026-01-05 09:00", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202601050815_202601050900_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ch_8b_202601050900_202601050945_dur_45_rm_b204", "Chemistry", "8B", "2026-01-05 09:00", "2026-01-05 09:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202601050900_202601050945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ma_7b_202601051000_202601051045_dur_45_rm_a102", "Mathematics", "7B", "2026-01-05 10:00", "2026-01-05 10:45", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202601051000_202601051045_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_9a_202601051100_202601051145_dur_45_rm_b205", "Chemistry", "9A", "2026-01-05 11:00", "2026-01-05 11:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202601051100_202601051145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ma_8c_202601051230_202601051315_dur_45_rm_a103", "Math", "8C", "2026-01-05 12:30", "2026-01-05 13:15", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202601051230_202601051315_dur_45_rm_a103");

    INSERT INTO Class VALUES("cl_ma_7a_202601120815_202601120900_dur_45_rm_a101", "Mathematics", "7A", "2026-01-12 08:15", "2026-01-12 09:00", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202601120815_202601120900_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ch_8b_202601120900_202601120945_dur_45_rm_b204", "Chemistry", "8B", "2026-01-12 09:00", "2026-01-12 09:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202601120900_202601120945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ma_7b_202601121000_202601121045_dur_45_rm_a102", "Mathematics", "7B", "2026-01-12 10:00", "2026-01-12 10:45", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202601121000_202601121045_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_9a_202601121100_202601121145_dur_45_rm_b205", "Chemistry", "9A", "2026-01-12 11:00", "2026-01-12 11:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202601121100_202601121145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ma_8c_202601121230_202601121315_dur_45_rm_a103", "Math", "8C", "2026-01-12 12:30", "2026-01-12 13:15", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202601121230_202601121315_dur_45_rm_a103");

    INSERT INTO Class VALUES("cl_ma_7a_202601190815_202601190900_dur_45_rm_a101", "Mathematics", "7A", "2026-01-19 08:15", "2026-01-19 09:00", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202601190815_202601190900_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ch_8b_202601190900_202601190945_dur_45_rm_b204", "Chemistry", "8B", "2026-01-19 09:00", "2026-01-19 09:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202601190900_202601190945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ma_7b_202601191000_202601191045_dur_45_rm_a102", "Mathematics", "7B", "2026-01-19 10:00", "2026-01-19 10:45", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202601191000_202601191045_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_9a_202601191100_202601191145_dur_45_rm_b205", "Chemistry", "9A", "2026-01-19 11:00", "2026-01-19 11:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202601191100_202601191145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ma_8c_202601191230_202601191315_dur_45_rm_a103", "Math", "8C", "2026-01-19 12:30", "2026-01-19 13:15", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202601191230_202601191315_dur_45_rm_a103");

    INSERT INTO Class VALUES("cl_ma_7a_202601260815_202601260900_dur_45_rm_a101", "Mathematics", "7A", "2026-01-26 08:15", "2026-01-26 09:00", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202601260815_202601260900_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ch_8b_202601260900_202601260945_dur_45_rm_b204", "Chemistry", "8B", "2026-01-26 09:00", "2026-01-26 09:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202601260900_202601260945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ma_7b_202601261000_202601261045_dur_45_rm_a102", "Mathematics", "7B", "2026-01-26 10:00", "2026-01-26 10:45", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202601261000_202601261045_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_9a_202601261100_202601261145_dur_45_rm_b205", "Chemistry", "9A", "2026-01-26 11:00", "2026-01-26 11:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202601261100_202601261145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ma_8c_202601261230_202601261315_dur_45_rm_a103", "Math", "8C", "2026-01-26 12:30", "2026-01-26 13:15", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202601261230_202601261315_dur_45_rm_a103");

    INSERT INTO Class VALUES("cl_ma_7a_202602020815_202602020900_dur_45_rm_a101", "Mathematics", "7A", "2026-02-02 08:15", "2026-02-02 09:00", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202602020815_202602020900_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ch_8b_202602020900_202602020945_dur_45_rm_b204", "Chemistry", "8B", "2026-02-02 09:00", "2026-02-02 09:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202602020900_202602020945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ma_7b_202602021000_202602021045_dur_45_rm_a102", "Mathematics", "7B", "2026-02-02 10:00", "2026-02-02 10:45", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202602021000_202602021045_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_9a_202602021100_202602021145_dur_45_rm_b205", "Chemistry", "9A", "2026-02-02 11:00", "2026-02-02 11:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202602021100_202602021145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ma_8c_202602021230_202602021315_dur_45_rm_a103", "Math", "8C", "2026-02-02 12:30", "2026-02-02 13:15", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202602021230_202602021315_dur_45_rm_a103");

    INSERT INTO Class VALUES("cl_ma_7a_202602090815_202602090900_dur_45_rm_a101", "Mathematics", "7A", "2026-02-09 08:15", "2026-02-09 09:00", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202602090815_202602090900_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ch_8b_202602090900_202602090945_dur_45_rm_b204", "Chemistry", "8B", "2026-02-09 09:00", "2026-02-09 09:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202602090900_202602090945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ma_7b_202602091000_202602091045_dur_45_rm_a102", "Mathematics", "7B", "2026-02-09 10:00", "2026-02-09 10:45", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202602091000_202602091045_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_9a_202602091100_202602091145_dur_45_rm_b205", "Chemistry", "9A", "2026-02-09 11:00", "2026-02-09 11:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202602091100_202602091145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ma_8c_202602091230_202602091315_dur_45_rm_a103", "Math", "8C", "2026-02-09 12:30", "2026-02-09 13:15", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202602091230_202602091315_dur_45_rm_a103");

    INSERT INTO Class VALUES("cl_ma_7a_202602160815_202602160900_dur_45_rm_a101", "Mathematics", "7A", "2026-02-16 08:15", "2026-02-16 09:00", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202602160815_202602160900_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ch_8b_202602160900_202602160945_dur_45_rm_b204", "Chemistry", "8B", "2026-02-16 09:00", "2026-02-16 09:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202602160900_202602160945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ma_7b_202602161000_202602161045_dur_45_rm_a102", "Mathematics", "7B", "2026-02-16 10:00", "2026-02-16 10:45", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202602161000_202602161045_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_9a_202602161100_202602161145_dur_45_rm_b205", "Chemistry", "9A", "2026-02-16 11:00", "2026-02-16 11:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202602161100_202602161145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ma_8c_202602161230_202602161315_dur_45_rm_a103", "Math", "8C", "2026-02-16 12:30", "2026-02-16 13:15", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202602161230_202602161315_dur_45_rm_a103");

    INSERT INTO Class VALUES("cl_ma_7a_202602230815_202602230900_dur_45_rm_a101", "Mathematics", "7A", "2026-02-23 08:15", "2026-02-23 09:00", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202602230815_202602230900_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ch_8b_202602230900_202602230945_dur_45_rm_b204", "Chemistry", "8B", "2026-02-23 09:00", "2026-02-23 09:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202602230900_202602230945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ma_7b_202602231000_202602231045_dur_45_rm_a102", "Mathematics", "7B", "2026-02-23 10:00", "2026-02-23 10:45", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202602231000_202602231045_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_9a_202602231100_202602231145_dur_45_rm_b205", "Chemistry", "9A", "2026-02-23 11:00", "2026-02-23 11:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202602231100_202602231145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ma_8c_202602231230_202602231315_dur_45_rm_a103", "Math", "8C", "2026-02-23 12:30", "2026-02-23 13:15", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202602231230_202602231315_dur_45_rm_a103");

    INSERT INTO Class VALUES("cl_ma_7a_202603020815_202603020900_dur_45_rm_a101", "Mathematics", "7A", "2026-03-02 08:15", "2026-03-02 09:00", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202603020815_202603020900_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ch_8b_202603020900_202603020945_dur_45_rm_b204", "Chemistry", "8B", "2026-03-02 09:00", "2026-03-02 09:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202603020900_202603020945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ma_7b_202603021000_202603021045_dur_45_rm_a102", "Mathematics", "7B", "2026-03-02 10:00", "2026-03-02 10:45", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202603021000_202603021045_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_9a_202603021100_202603021145_dur_45_rm_b205", "Chemistry", "9A", "2026-03-02 11:00", "2026-03-02 11:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202603021100_202603021145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ma_8c_202603021230_202603021315_dur_45_rm_a103", "Math", "8C", "2026-03-02 12:30", "2026-03-02 13:15", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202603021230_202603021315_dur_45_rm_a103");

    INSERT INTO Class VALUES("cl_ma_7a_202603090815_202603090900_dur_45_rm_a101", "Mathematics", "7A", "2026-03-09 08:15", "2026-03-09 09:00", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202603090815_202603090900_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ch_8b_202603090900_202603090945_dur_45_rm_b204", "Chemistry", "8B", "2026-03-09 09:00", "2026-03-09 09:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202603090900_202603090945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ma_7b_202603091000_202603091045_dur_45_rm_a102", "Mathematics", "7B", "2026-03-09 10:00", "2026-03-09 10:45", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202603091000_202603091045_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_9a_202603091100_202603091145_dur_45_rm_b205", "Chemistry", "9A", "2026-03-09 11:00", "2026-03-09 11:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202603091100_202603091145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ma_8c_202603091230_202603091315_dur_45_rm_a103", "Math", "8C", "2026-03-09 12:30", "2026-03-09 13:15", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202603091230_202603091315_dur_45_rm_a103");

    INSERT INTO Class VALUES("cl_ma_7a_202603160815_202603160900_dur_45_rm_a101", "Mathematics", "7A", "2026-03-16 08:15", "2026-03-16 09:00", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202603160815_202603160900_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ch_8b_202603160900_202603160945_dur_45_rm_b204", "Chemistry", "8B", "2026-03-16 09:00", "2026-03-16 09:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202603160900_202603160945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ma_7b_202603161000_202603161045_dur_45_rm_a102", "Mathematics", "7B", "2026-03-16 10:00", "2026-03-16 10:45", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202603161000_202603161045_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_9a_202603161100_202603161145_dur_45_rm_b205", "Chemistry", "9A", "2026-03-16 11:00", "2026-03-16 11:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202603161100_202603161145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ma_8c_202603161230_202603161315_dur_45_rm_a103", "Math", "8C", "2026-03-16 12:30", "2026-03-16 13:15", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202603161230_202603161315_dur_45_rm_a103");

    INSERT INTO Class VALUES("cl_ma_7a_202603230815_202603230900_dur_45_rm_a101", "Mathematics", "7A", "2026-03-23 08:15", "2026-03-23 09:00", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202603230815_202603230900_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ch_8b_202603230900_202603230945_dur_45_rm_b204", "Chemistry", "8B", "2026-03-23 09:00", "2026-03-23 09:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202603230900_202603230945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ma_7b_202603231000_202603231045_dur_45_rm_a102", "Mathematics", "7B", "2026-03-23 10:00", "2026-03-23 10:45", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202603231000_202603231045_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_9a_202603231100_202603231145_dur_45_rm_b205", "Chemistry", "9A", "2026-03-23 11:00", "2026-03-23 11:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202603231100_202603231145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ma_8c_202603231230_202603231315_dur_45_rm_a103", "Math", "8C", "2026-03-23 12:30", "2026-03-23 13:15", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202603231230_202603231315_dur_45_rm_a103");

    INSERT INTO Class VALUES("cl_ph_7c_202511110815_202511110900_dur_45_rm_a104", "Physics", "7C", "2025-11-11 08:15", "2025-11-11 09:00", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202511110815_202511110900_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ph_8a_202511110900_202511110945_dur_45_rm_a105", "Physics", "8A", "2025-11-11 09:00", "2025-11-11 09:45", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202511110900_202511110945_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ph_9b_202511111000_202511111045_dur_45_rm_gym1", "Physics", "9B", "2025-11-11 10:00", "2025-11-11 10:45", "45", "Gym1", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202511111000_202511111045_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ma_7a_202511111100_202511111145_dur_45_rm_a101", "Mathematics", "7A", "2025-11-11 11:00", "2025-11-11 11:45", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202511111100_202511111145_dur_45_rm_a101");

    INSERT INTO Class VALUES("cl_ph_7c_202511180815_202511180900_dur_45_rm_a104", "Physics", "7C", "2025-11-18 08:15", "2025-11-18 09:00", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202511180815_202511180900_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ph_8a_202511180900_202511180945_dur_45_rm_a105", "Physics", "8A", "2025-11-18 09:00", "2025-11-18 09:45", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202511180900_202511180945_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ph_9b_202511181000_202511181045_dur_45_rm_gym1", "Physics", "9B", "2025-11-18 10:00", "2025-11-18 10:45", "45", "Gym1", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202511181000_202511181045_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ma_7a_202511181100_202511181145_dur_45_rm_a101", "Mathematics", "7A", "2025-11-18 11:00", "2025-11-18 11:45", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202511181100_202511181145_dur_45_rm_a101");

    INSERT INTO Class VALUES("cl_ph_7c_202511250815_202511250900_dur_45_rm_a104", "Physics", "7C", "2025-11-25 08:15", "2025-11-25 09:00", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202511250815_202511250900_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ph_8a_202511250900_202511250945_dur_45_rm_a105", "Physics", "8A", "2025-11-25 09:00", "2025-11-25 09:45", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202511250900_202511250945_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ph_9b_202511251000_202511251045_dur_45_rm_gym1", "Physics", "9B", "2025-11-25 10:00", "2025-11-25 10:45", "45", "Gym1", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202511251000_202511251045_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ma_7a_202511251100_202511251145_dur_45_rm_a101", "Mathematics", "7A", "2025-11-25 11:00", "2025-11-25 11:45", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202511251100_202511251145_dur_45_rm_a101");

    INSERT INTO Class VALUES("cl_ph_7c_202512020815_202512020900_dur_45_rm_a104", "Physics", "7C", "2025-12-02 08:15", "2025-12-02 09:00", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202512020815_202512020900_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ph_8a_202512020900_202512020945_dur_45_rm_a105", "Physics", "8A", "2025-12-02 09:00", "2025-12-02 09:45", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202512020900_202512020945_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ph_9b_202512021000_202512021045_dur_45_rm_gym1", "Physics", "9B", "2025-12-02 10:00", "2025-12-02 10:45", "45", "Gym1", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202512021000_202512021045_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ma_7a_202512021100_202512021145_dur_45_rm_a101", "Mathematics", "7A", "2025-12-02 11:00", "2025-12-02 11:45", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202512021100_202512021145_dur_45_rm_a101");

    INSERT INTO Class VALUES("cl_ph_7c_202512090815_202512090900_dur_45_rm_a104", "Physics", "7C", "2025-12-09 08:15", "2025-12-09 09:00", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202512090815_202512090900_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ph_8a_202512090900_202512090945_dur_45_rm_a105", "Physics", "8A", "2025-12-09 09:00", "2025-12-09 09:45", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202512090900_202512090945_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ph_9b_202512091000_202512091045_dur_45_rm_gym1", "Physics", "9B", "2025-12-09 10:00", "2025-12-09 10:45", "45", "Gym1", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202512091000_202512091045_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ma_7a_202512091100_202512091145_dur_45_rm_a101", "Mathematics", "7A", "2025-12-09 11:00", "2025-12-09 11:45", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202512091100_202512091145_dur_45_rm_a101");

    INSERT INTO Class VALUES("cl_ph_7c_202512160815_202512160900_dur_45_rm_a104", "Physics", "7C", "2025-12-16 08:15", "2025-12-16 09:00", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202512160815_202512160900_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ph_8a_202512160900_202512160945_dur_45_rm_a105", "Physics", "8A", "2025-12-16 09:00", "2025-12-16 09:45", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202512160900_202512160945_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ph_9b_202512161000_202512161045_dur_45_rm_gym1", "Physics", "9B", "2025-12-16 10:00", "2025-12-16 10:45", "45", "Gym1", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202512161000_202512161045_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ma_7a_202512161100_202512161145_dur_45_rm_a101", "Mathematics", "7A", "2025-12-16 11:00", "2025-12-16 11:45", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202512161100_202512161145_dur_45_rm_a101");

    INSERT INTO Class VALUES("cl_ph_7c_202512230815_202512230900_dur_45_rm_a104", "Physics", "7C", "2025-12-23 08:15", "2025-12-23 09:00", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202512230815_202512230900_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ph_8a_202512230900_202512230945_dur_45_rm_a105", "Physics", "8A", "2025-12-23 09:00", "2025-12-23 09:45", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202512230900_202512230945_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ph_9b_202512231000_202512231045_dur_45_rm_gym1", "Physics", "9B", "2025-12-23 10:00", "2025-12-23 10:45", "45", "Gym1", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202512231000_202512231045_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ma_7a_202512231100_202512231145_dur_45_rm_a101", "Mathematics", "7A", "2025-12-23 11:00", "2025-12-23 11:45", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202512231100_202512231145_dur_45_rm_a101");

    INSERT INTO Class VALUES("cl_ph_7c_202512300815_202512300900_dur_45_rm_a104", "Physics", "7C", "2025-12-30 08:15", "2025-12-30 09:00", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202512300815_202512300900_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ph_8a_202512300900_202512300945_dur_45_rm_a105", "Physics", "8A", "2025-12-30 09:00", "2025-12-30 09:45", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202512300900_202512300945_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ph_9b_202512301000_202512301045_dur_45_rm_gym1", "Physics", "9B", "2025-12-30 10:00", "2025-12-30 10:45", "45", "Gym1", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202512301000_202512301045_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ma_7a_202512301100_202512301145_dur_45_rm_a101", "Mathematics", "7A", "2025-12-30 11:00", "2025-12-30 11:45", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202512301100_202512301145_dur_45_rm_a101");

    INSERT INTO Class VALUES("cl_ph_7c_202601060815_202601060900_dur_45_rm_a104", "Physics", "7C", "2026-01-06 08:15", "2026-01-06 09:00", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202601060815_202601060900_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ph_8a_202601060900_202601060945_dur_45_rm_a105", "Physics", "8A", "2026-01-06 09:00", "2026-01-06 09:45", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202601060900_202601060945_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ph_9b_202601061000_202601061045_dur_45_rm_gym1", "Physics", "9B", "2026-01-06 10:00", "2026-01-06 10:45", "45", "Gym1", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202601061000_202601061045_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ma_7a_202601061100_202601061145_dur_45_rm_a101", "Mathematics", "7A", "2026-01-06 11:00", "2026-01-06 11:45", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202601061100_202601061145_dur_45_rm_a101");

    INSERT INTO Class VALUES("cl_ph_7c_202601130815_202601130900_dur_45_rm_a104", "Physics", "7C", "2026-01-13 08:15", "2026-01-13 09:00", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202601130815_202601130900_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ph_8a_202601130900_202601130945_dur_45_rm_a105", "Physics", "8A", "2026-01-13 09:00", "2026-01-13 09:45", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202601130900_202601130945_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ph_9b_202601131000_202601131045_dur_45_rm_gym1", "Physics", "9B", "2026-01-13 10:00", "2026-01-13 10:45", "45", "Gym1", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202601131000_202601131045_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ma_7a_202601131100_202601131145_dur_45_rm_a101", "Mathematics", "7A", "2026-01-13 11:00", "2026-01-13 11:45", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202601131100_202601131145_dur_45_rm_a101");

    INSERT INTO Class VALUES("cl_ph_7c_202601200815_202601200900_dur_45_rm_a104", "Physics", "7C", "2026-01-20 08:15", "2026-01-20 09:00", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202601200815_202601200900_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ph_8a_202601200900_202601200945_dur_45_rm_a105", "Physics", "8A", "2026-01-20 09:00", "2026-01-20 09:45", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202601200900_202601200945_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ph_9b_202601201000_202601201045_dur_45_rm_gym1", "Physics", "9B", "2026-01-20 10:00", "2026-01-20 10:45", "45", "Gym1", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202601201000_202601201045_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ma_7a_202601201100_202601201145_dur_45_rm_a101", "Mathematics", "7A", "2026-01-20 11:00", "2026-01-20 11:45", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202601201100_202601201145_dur_45_rm_a101");

    INSERT INTO Class VALUES("cl_ph_7c_202601270815_202601270900_dur_45_rm_a104", "Physics", "7C", "2026-01-27 08:15", "2026-01-27 09:00", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202601270815_202601270900_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ph_8a_202601270900_202601270945_dur_45_rm_a105", "Physics", "8A", "2026-01-27 09:00", "2026-01-27 09:45", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202601270900_202601270945_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ph_9b_202601271000_202601271045_dur_45_rm_gym1", "Physics", "9B", "2026-01-27 10:00", "2026-01-27 10:45", "45", "Gym1", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202601271000_202601271045_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ma_7a_202601271100_202601271145_dur_45_rm_a101", "Mathematics", "7A", "2026-01-27 11:00", "2026-01-27 11:45", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202601271100_202601271145_dur_45_rm_a101");

    INSERT INTO Class VALUES("cl_ph_7c_202602030815_202602030900_dur_45_rm_a104", "Physics", "7C", "2026-02-03 08:15", "2026-02-03 09:00", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202602030815_202602030900_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ph_8a_202602030900_202602030945_dur_45_rm_a105", "Physics", "8A", "2026-02-03 09:00", "2026-02-03 09:45", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202602030900_202602030945_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ph_9b_202602031000_202602031045_dur_45_rm_gym1", "Physics", "9B", "2026-02-03 10:00", "2026-02-03 10:45", "45", "Gym1", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202602031000_202602031045_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ma_7a_202602031100_202602031145_dur_45_rm_a101", "Mathematics", "7A", "2026-02-03 11:00", "2026-02-03 11:45", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202602031100_202602031145_dur_45_rm_a101");

    INSERT INTO Class VALUES("cl_ph_7c_202602100815_202602100900_dur_45_rm_a104", "Physics", "7C", "2026-02-10 08:15", "2026-02-10 09:00", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202602100815_202602100900_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ph_8a_202602100900_202602100945_dur_45_rm_a105", "Physics", "8A", "2026-02-10 09:00", "2026-02-10 09:45", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202602100900_202602100945_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ph_9b_202602101000_202602101045_dur_45_rm_gym1", "Physics", "9B", "2026-02-10 10:00", "2026-02-10 10:45", "45", "Gym1", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202602101000_202602101045_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ma_7a_202602101100_202602101145_dur_45_rm_a101", "Mathematics", "7A", "2026-02-10 11:00", "2026-02-10 11:45", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202602101100_202602101145_dur_45_rm_a101");

    INSERT INTO Class VALUES("cl_ph_7c_202602170815_202602170900_dur_45_rm_a104", "Physics", "7C", "2026-02-17 08:15", "2026-02-17 09:00", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202602170815_202602170900_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ph_8a_202602170900_202602170945_dur_45_rm_a105", "Physics", "8A", "2026-02-17 09:00", "2026-02-17 09:45", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202602170900_202602170945_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ph_9b_202602171000_202602171045_dur_45_rm_gym1", "Physics", "9B", "2026-02-17 10:00", "2026-02-17 10:45", "45", "Gym1", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202602171000_202602171045_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ma_7a_202602171100_202602171145_dur_45_rm_a101", "Mathematics", "7A", "2026-02-17 11:00", "2026-02-17 11:45", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202602171100_202602171145_dur_45_rm_a101");

    INSERT INTO Class VALUES("cl_ph_7c_202602240815_202602240900_dur_45_rm_a104", "Physics", "7C", "2026-02-24 08:15", "2026-02-24 09:00", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202602240815_202602240900_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ph_8a_202602240900_202602240945_dur_45_rm_a105", "Physics", "8A", "2026-02-24 09:00", "2026-02-24 09:45", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202602240900_202602240945_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ph_9b_202602241000_202602241045_dur_45_rm_gym1", "Physics", "9B", "2026-02-24 10:00", "2026-02-24 10:45", "45", "Gym1", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202602241000_202602241045_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ma_7a_202602241100_202602241145_dur_45_rm_a101", "Mathematics", "7A", "2026-02-24 11:00", "2026-02-24 11:45", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202602241100_202602241145_dur_45_rm_a101");

    INSERT INTO Class VALUES("cl_ph_7c_202603030815_202603030900_dur_45_rm_a104", "Physics", "7C", "2026-03-03 08:15", "2026-03-03 09:00", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202603030815_202603030900_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ph_8a_202603030900_202603030945_dur_45_rm_a105", "Physics", "8A", "2026-03-03 09:00", "2026-03-03 09:45", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202603030900_202603030945_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ph_9b_202603031000_202603031045_dur_45_rm_gym1", "Physics", "9B", "2026-03-03 10:00", "2026-03-03 10:45", "45", "Gym1", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202603031000_202603031045_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ma_7a_202603031100_202603031145_dur_45_rm_a101", "Mathematics", "7A", "2026-03-03 11:00", "2026-03-03 11:45", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202603031100_202603031145_dur_45_rm_a101");

    INSERT INTO Class VALUES("cl_ph_7c_202603100815_202603100900_dur_45_rm_a104", "Physics", "7C", "2026-03-10 08:15", "2026-03-10 09:00", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202603100815_202603100900_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ph_8a_202603100900_202603100945_dur_45_rm_a105", "Physics", "8A", "2026-03-10 09:00", "2026-03-10 09:45", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202603100900_202603100945_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ph_9b_202603101000_202603101045_dur_45_rm_gym1", "Physics", "9B", "2026-03-10 10:00", "2026-03-10 10:45", "45", "Gym1", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202603101000_202603101045_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ma_7a_202603101100_202603101145_dur_45_rm_a101", "Mathematics", "7A", "2026-03-10 11:00", "2026-03-10 11:45", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202603101100_202603101145_dur_45_rm_a101");

    INSERT INTO Class VALUES("cl_ph_7c_202603170815_202603170900_dur_45_rm_a104", "Physics", "7C", "2026-03-17 08:15", "2026-03-17 09:00", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202603170815_202603170900_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ph_8a_202603170900_202603170945_dur_45_rm_a105", "Physics", "8A", "2026-03-17 09:00", "2026-03-17 09:45", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202603170900_202603170945_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ph_9b_202603171000_202603171045_dur_45_rm_gym1", "Physics", "9B", "2026-03-17 10:00", "2026-03-17 10:45", "45", "Gym1", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202603171000_202603171045_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ma_7a_202603171100_202603171145_dur_45_rm_a101", "Mathematics", "7A", "2026-03-17 11:00", "2026-03-17 11:45", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202603171100_202603171145_dur_45_rm_a101");

    INSERT INTO Class VALUES("cl_ph_7c_202603240815_202603240900_dur_45_rm_a104", "Physics", "7C", "2026-03-24 08:15", "2026-03-24 09:00", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202603240815_202603240900_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ph_8a_202603240900_202603240945_dur_45_rm_a105", "Physics", "8A", "2026-03-24 09:00", "2026-03-24 09:45", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202603240900_202603240945_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ph_9b_202603241000_202603241045_dur_45_rm_gym1", "Physics", "9B", "2026-03-24 10:00", "2026-03-24 10:45", "45", "Gym1", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202603241000_202603241045_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ma_7a_202603241100_202603241145_dur_45_rm_a101", "Mathematics", "7A", "2026-03-24 11:00", "2026-03-24 11:45", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202603241100_202603241145_dur_45_rm_a101");

    INSERT INTO Class VALUES("cl_ma_8c_202511120815_202511120900_dur_45_rm_a103", "Mathematics", "8C", "2025-11-12 08:15", "2025-11-12 09:00", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202511120815_202511120900_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202511120900_202511120945_dur_45_rm_a102", "Mathematics", "7B", "2025-11-12 09:00", "2025-11-12 09:45", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202511120900_202511120945_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_8b_202511121000_202511121045_dur_45_rm_b204", "Chemistry", "8B", "2025-11-12 10:00", "2025-11-12 10:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202511121000_202511121045_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202511121100_202511121145_dur_45_rm_b205", "Chemistry", "9A", "2025-11-12 11:00", "2025-11-12 11:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202511121100_202511121145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_8a_202511121230_202511121315_dur_45_rm_a105", "Physics", "8A", "2025-11-12 12:30", "2025-11-12 13:15", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202511121230_202511121315_dur_45_rm_a105");

    INSERT INTO Class VALUES("cl_ma_8c_202511190815_202511190900_dur_45_rm_a103", "Mathematics", "8C", "2025-11-19 08:15", "2025-11-19 09:00", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202511190815_202511190900_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202511190900_202511190945_dur_45_rm_a102", "Mathematics", "7B", "2025-11-19 09:00", "2025-11-19 09:45", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202511190900_202511190945_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_8b_202511191000_202511191045_dur_45_rm_b204", "Chemistry", "8B", "2025-11-19 10:00", "2025-11-19 10:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202511191000_202511191045_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202511191100_202511191145_dur_45_rm_b205", "Chemistry", "9A", "2025-11-19 11:00", "2025-11-19 11:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202511191100_202511191145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_8a_202511191230_202511191315_dur_45_rm_a105", "Physics", "8A", "2025-11-19 12:30", "2025-11-19 13:15", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202511191230_202511191315_dur_45_rm_a105");

    INSERT INTO Class VALUES("cl_ma_8c_202511260815_202511260900_dur_45_rm_a103", "Mathematics", "8C", "2025-11-26 08:15", "2025-11-26 09:00", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202511260815_202511260900_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202511260900_202511260945_dur_45_rm_a102", "Mathematics", "7B", "2025-11-26 09:00", "2025-11-26 09:45", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202511260900_202511260945_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_8b_202511261000_202511261045_dur_45_rm_b204", "Chemistry", "8B", "2025-11-26 10:00", "2025-11-26 10:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202511261000_202511261045_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202511261100_202511261145_dur_45_rm_b205", "Chemistry", "9A", "2025-11-26 11:00", "2025-11-26 11:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202511261100_202511261145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_8a_202511261230_202511261315_dur_45_rm_a105", "Physics", "8A", "2025-11-26 12:30", "2025-11-26 13:15", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202511261230_202511261315_dur_45_rm_a105");

    INSERT INTO Class VALUES("cl_ma_8c_202512030815_202512030900_dur_45_rm_a103", "Mathematics", "8C", "2025-12-03 08:15", "2025-12-03 09:00", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202512030815_202512030900_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202512030900_202512030945_dur_45_rm_a102", "Mathematics", "7B", "2025-12-03 09:00", "2025-12-03 09:45", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202512030900_202512030945_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_8b_202512031000_202512031045_dur_45_rm_b204", "Chemistry", "8B", "2025-12-03 10:00", "2025-12-03 10:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202512031000_202512031045_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202512031100_202512031145_dur_45_rm_b205", "Chemistry", "9A", "2025-12-03 11:00", "2025-12-03 11:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202512031100_202512031145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_8a_202512031230_202512031315_dur_45_rm_a105", "Physics", "8A", "2025-12-03 12:30", "2025-12-03 13:15", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202512031230_202512031315_dur_45_rm_a105");

    INSERT INTO Class VALUES("cl_ma_8c_202512100815_202512100900_dur_45_rm_a103", "Mathematics", "8C", "2025-12-10 08:15", "2025-12-10 09:00", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202512100815_202512100900_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202512100900_202512100945_dur_45_rm_a102", "Mathematics", "7B", "2025-12-10 09:00", "2025-12-10 09:45", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202512100900_202512100945_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_8b_202512101000_202512101045_dur_45_rm_b204", "Chemistry", "8B", "2025-12-10 10:00", "2025-12-10 10:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202512101000_202512101045_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202512101100_202512101145_dur_45_rm_b205", "Chemistry", "9A", "2025-12-10 11:00", "2025-12-10 11:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202512101100_202512101145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_8a_202512101230_202512101315_dur_45_rm_a105", "Physics", "8A", "2025-12-10 12:30", "2025-12-10 13:15", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202512101230_202512101315_dur_45_rm_a105");

    INSERT INTO Class VALUES("cl_ma_8c_202512170815_202512170900_dur_45_rm_a103", "Mathematics", "8C", "2025-12-17 08:15", "2025-12-17 09:00", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202512170815_202512170900_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202512170900_202512170945_dur_45_rm_a102", "Mathematics", "7B", "2025-12-17 09:00", "2025-12-17 09:45", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202512170900_202512170945_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_8b_202512171000_202512171045_dur_45_rm_b204", "Chemistry", "8B", "2025-12-17 10:00", "2025-12-17 10:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202512171000_202512171045_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202512171100_202512171145_dur_45_rm_b205", "Chemistry", "9A", "2025-12-17 11:00", "2025-12-17 11:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202512171100_202512171145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_8a_202512171230_202512171315_dur_45_rm_a105", "Physics", "8A", "2025-12-17 12:30", "2025-12-17 13:15", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202512171230_202512171315_dur_45_rm_a105");

    INSERT INTO Class VALUES("cl_ma_8c_202512240815_202512240900_dur_45_rm_a103", "Mathematics", "8C", "2025-12-24 08:15", "2025-12-24 09:00", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202512240815_202512240900_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202512240900_202512240945_dur_45_rm_a102", "Mathematics", "7B", "2025-12-24 09:00", "2025-12-24 09:45", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202512240900_202512240945_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_8b_202512241000_202512241045_dur_45_rm_b204", "Chemistry", "8B", "2025-12-24 10:00", "2025-12-24 10:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202512241000_202512241045_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202512241100_202512241145_dur_45_rm_b205", "Chemistry", "9A", "2025-12-24 11:00", "2025-12-24 11:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202512241100_202512241145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_8a_202512241230_202512241315_dur_45_rm_a105", "Physics", "8A", "2025-12-24 12:30", "2025-12-24 13:15", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202512241230_202512241315_dur_45_rm_a105");

    INSERT INTO Class VALUES("cl_ma_8c_202512310815_202512310900_dur_45_rm_a103", "Mathematics", "8C", "2025-12-31 08:15", "2025-12-31 09:00", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202512310815_202512310900_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202512310900_202512310945_dur_45_rm_a102", "Mathematics", "7B", "2025-12-31 09:00", "2025-12-31 09:45", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202512310900_202512310945_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_8b_202512311000_202512311045_dur_45_rm_b204", "Chemistry", "8B", "2025-12-31 10:00", "2025-12-31 10:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202512311000_202512311045_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202512311100_202512311145_dur_45_rm_b205", "Chemistry", "9A", "2025-12-31 11:00", "2025-12-31 11:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202512311100_202512311145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_8a_202512311230_202512311315_dur_45_rm_a105", "Physics", "8A", "2025-12-31 12:30", "2025-12-31 13:15", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202512311230_202512311315_dur_45_rm_a105");

    INSERT INTO Class VALUES("cl_ma_8c_202601070815_202601070900_dur_45_rm_a103", "Mathematics", "8C", "2026-01-07 08:15", "2026-01-07 09:00", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202601070815_202601070900_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202601070900_202601070945_dur_45_rm_a102", "Mathematics", "7B", "2026-01-07 09:00", "2026-01-07 09:45", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202601070900_202601070945_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_8b_202601071000_202601071045_dur_45_rm_b204", "Chemistry", "8B", "2026-01-07 10:00", "2026-01-07 10:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202601071000_202601071045_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202601071100_202601071145_dur_45_rm_b205", "Chemistry", "9A", "2026-01-07 11:00", "2026-01-07 11:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202601071100_202601071145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_8a_202601071230_202601071315_dur_45_rm_a105", "Physics", "8A", "2026-01-07 12:30", "2026-01-07 13:15", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202601071230_202601071315_dur_45_rm_a105");

    INSERT INTO Class VALUES("cl_ma_8c_202601140815_202601140900_dur_45_rm_a103", "Mathematics", "8C", "2026-01-14 08:15", "2026-01-14 09:00", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202601140815_202601140900_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202601140900_202601140945_dur_45_rm_a102", "Mathematics", "7B", "2026-01-14 09:00", "2026-01-14 09:45", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202601140900_202601140945_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_8b_202601141000_202601141045_dur_45_rm_b204", "Chemistry", "8B", "2026-01-14 10:00", "2026-01-14 10:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202601141000_202601141045_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202601141100_202601141145_dur_45_rm_b205", "Chemistry", "9A", "2026-01-14 11:00", "2026-01-14 11:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202601141100_202601141145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_8a_202601141230_202601141315_dur_45_rm_a105", "Physics", "8A", "2026-01-14 12:30", "2026-01-14 13:15", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202601141230_202601141315_dur_45_rm_a105");

    INSERT INTO Class VALUES("cl_ma_8c_202601210815_202601210900_dur_45_rm_a103", "Mathematics", "8C", "2026-01-21 08:15", "2026-01-21 09:00", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202601210815_202601210900_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202601210900_202601210945_dur_45_rm_a102", "Mathematics", "7B", "2026-01-21 09:00", "2026-01-21 09:45", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202601210900_202601210945_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_8b_202601211000_202601211045_dur_45_rm_b204", "Chemistry", "8B", "2026-01-21 10:00", "2026-01-21 10:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202601211000_202601211045_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202601211100_202601211145_dur_45_rm_b205", "Chemistry", "9A", "2026-01-21 11:00", "2026-01-21 11:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202601211100_202601211145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_8a_202601211230_202601211315_dur_45_rm_a105", "Physics", "8A", "2026-01-21 12:30", "2026-01-21 13:15", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202601211230_202601211315_dur_45_rm_a105");

    INSERT INTO Class VALUES("cl_ma_8c_202601280815_202601280900_dur_45_rm_a103", "Mathematics", "8C", "2026-01-28 08:15", "2026-01-28 09:00", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202601280815_202601280900_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202601280900_202601280945_dur_45_rm_a102", "Mathematics", "7B", "2026-01-28 09:00", "2026-01-28 09:45", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202601280900_202601280945_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_8b_202601281000_202601281045_dur_45_rm_b204", "Chemistry", "8B", "2026-01-28 10:00", "2026-01-28 10:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202601281000_202601281045_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202601281100_202601281145_dur_45_rm_b205", "Chemistry", "9A", "2026-01-28 11:00", "2026-01-28 11:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202601281100_202601281145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_8a_202601281230_202601281315_dur_45_rm_a105", "Physics", "8A", "2026-01-28 12:30", "2026-01-28 13:15", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202601281230_202601281315_dur_45_rm_a105");

    INSERT INTO Class VALUES("cl_ma_8c_202602040815_202602040900_dur_45_rm_a103", "Mathematics", "8C", "2026-02-04 08:15", "2026-02-04 09:00", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202602040815_202602040900_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202602040900_202602040945_dur_45_rm_a102", "Mathematics", "7B", "2026-02-04 09:00", "2026-02-04 09:45", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202602040900_202602040945_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_8b_202602041000_202602041045_dur_45_rm_b204", "Chemistry", "8B", "2026-02-04 10:00", "2026-02-04 10:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202602041000_202602041045_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202602041100_202602041145_dur_45_rm_b205", "Chemistry", "9A", "2026-02-04 11:00", "2026-02-04 11:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202602041100_202602041145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_8a_202602041230_202602041315_dur_45_rm_a105", "Physics", "8A", "2026-02-04 12:30", "2026-02-04 13:15", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202602041230_202602041315_dur_45_rm_a105");

    INSERT INTO Class VALUES("cl_ma_8c_202602110815_202602110900_dur_45_rm_a103", "Mathematics", "8C", "2026-02-11 08:15", "2026-02-11 09:00", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202602110815_202602110900_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202602110900_202602110945_dur_45_rm_a102", "Mathematics", "7B", "2026-02-11 09:00", "2026-02-11 09:45", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202602110900_202602110945_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_8b_202602111000_202602111045_dur_45_rm_b204", "Chemistry", "8B", "2026-02-11 10:00", "2026-02-11 10:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202602111000_202602111045_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202602111100_202602111145_dur_45_rm_b205", "Chemistry", "9A", "2026-02-11 11:00", "2026-02-11 11:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202602111100_202602111145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_8a_202602111230_202602111315_dur_45_rm_a105", "Physics", "8A", "2026-02-11 12:30", "2026-02-11 13:15", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202602111230_202602111315_dur_45_rm_a105");

    INSERT INTO Class VALUES("cl_ma_8c_202602180815_202602180900_dur_45_rm_a103", "Mathematics", "8C", "2026-02-18 08:15", "2026-02-18 09:00", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202602180815_202602180900_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202602180900_202602180945_dur_45_rm_a102", "Mathematics", "7B", "2026-02-18 09:00", "2026-02-18 09:45", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202602180900_202602180945_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_8b_202602181000_202602181045_dur_45_rm_b204", "Chemistry", "8B", "2026-02-18 10:00", "2026-02-18 10:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202602181000_202602181045_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202602181100_202602181145_dur_45_rm_b205", "Chemistry", "9A", "2026-02-18 11:00", "2026-02-18 11:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202602181100_202602181145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_8a_202602181230_202602181315_dur_45_rm_a105", "Physics", "8A", "2026-02-18 12:30", "2026-02-18 13:15", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202602181230_202602181315_dur_45_rm_a105");

    INSERT INTO Class VALUES("cl_ma_8c_202602250815_202602250900_dur_45_rm_a103", "Mathematics", "8C", "2026-02-25 08:15", "2026-02-25 09:00", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202602250815_202602250900_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202602250900_202602250945_dur_45_rm_a102", "Mathematics", "7B", "2026-02-25 09:00", "2026-02-25 09:45", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202602250900_202602250945_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_8b_202602251000_202602251045_dur_45_rm_b204", "Chemistry", "8B", "2026-02-25 10:00", "2026-02-25 10:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202602251000_202602251045_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202602251100_202602251145_dur_45_rm_b205", "Chemistry", "9A", "2026-02-25 11:00", "2026-02-25 11:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202602251100_202602251145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_8a_202602251230_202602251315_dur_45_rm_a105", "Physics", "8A", "2026-02-25 12:30", "2026-02-25 13:15", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202602251230_202602251315_dur_45_rm_a105");

    INSERT INTO Class VALUES("cl_ma_8c_202603040815_202603040900_dur_45_rm_a103", "Mathematics", "8C", "2026-03-04 08:15", "2026-03-04 09:00", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202603040815_202603040900_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202603040900_202603040945_dur_45_rm_a102", "Mathematics", "7B", "2026-03-04 09:00", "2026-03-04 09:45", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202603040900_202603040945_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_8b_202603041000_202603041045_dur_45_rm_b204", "Chemistry", "8B", "2026-03-04 10:00", "2026-03-04 10:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202603041000_202603041045_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202603041100_202603041145_dur_45_rm_b205", "Chemistry", "9A", "2026-03-04 11:00", "2026-03-04 11:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202603041100_202603041145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_8a_202603041230_202603041315_dur_45_rm_a105", "Physics", "8A", "2026-03-04 12:30", "2026-03-04 13:15", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202603041230_202603041315_dur_45_rm_a105");

    INSERT INTO Class VALUES("cl_ma_8c_202603110815_202603110900_dur_45_rm_a103", "Mathematics", "8C", "2026-03-11 08:15", "2026-03-11 09:00", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202603110815_202603110900_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202603110900_202603110945_dur_45_rm_a102", "Mathematics", "7B", "2026-03-11 09:00", "2026-03-11 09:45", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202603110900_202603110945_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_8b_202603111000_202603111045_dur_45_rm_b204", "Chemistry", "8B", "2026-03-11 10:00", "2026-03-11 10:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202603111000_202603111045_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202603111100_202603111145_dur_45_rm_b205", "Chemistry", "9A", "2026-03-11 11:00", "2026-03-11 11:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202603111100_202603111145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_8a_202603111230_202603111315_dur_45_rm_a105", "Physics", "8A", "2026-03-11 12:30", "2026-03-11 13:15", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202603111230_202603111315_dur_45_rm_a105");

    INSERT INTO Class VALUES("cl_ma_8c_202603180815_202603180900_dur_45_rm_a103", "Mathematics", "8C", "2026-03-18 08:15", "2026-03-18 09:00", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202603180815_202603180900_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202603180900_202603180945_dur_45_rm_a102", "Mathematics", "7B", "2026-03-18 09:00", "2026-03-18 09:45", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202603180900_202603180945_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_8b_202603181000_202603181045_dur_45_rm_b204", "Chemistry", "8B", "2026-03-18 10:00", "2026-03-18 10:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202603181000_202603181045_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202603181100_202603181145_dur_45_rm_b205", "Chemistry", "9A", "2026-03-18 11:00", "2026-03-18 11:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202603181100_202603181145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_8a_202603181230_202603181315_dur_45_rm_a105", "Physics", "8A", "2026-03-18 12:30", "2026-03-18 13:15", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202603181230_202603181315_dur_45_rm_a105");

    INSERT INTO Class VALUES("cl_ma_8c_202603250815_202603250900_dur_45_rm_a103", "Mathematics", "8C", "2026-03-25 08:15", "2026-03-25 09:00", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202603250815_202603250900_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202603250900_202603250945_dur_45_rm_a102", "Mathematics", "7B", "2026-03-25 09:00", "2026-03-25 09:45", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202603250900_202603250945_dur_45_rm_a102");
    INSERT INTO Class VALUES("cl_ch_8b_202603251000_202603251045_dur_45_rm_b204", "Chemistry", "8B", "2026-03-25 10:00", "2026-03-25 10:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202603251000_202603251045_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202603251100_202603251145_dur_45_rm_b205", "Chemistry", "9A", "2026-03-25 11:00", "2026-03-25 11:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202603251100_202603251145_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_8a_202603251230_202603251315_dur_45_rm_a105", "Physics", "8A", "2026-03-25 12:30", "2026-03-25 13:15", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202603251230_202603251315_dur_45_rm_a105");

    INSERT INTO Class VALUES("cl_ph_9b_202511130815_202511130900_dur_45_rm_gym1", "Physics", "9B", "2025-11-13 08:15", "2025-11-13 09:00", "45", "Gym1", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202511130815_202511130900_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ph_7c_202511130900_202511130945_dur_45_rm_a104", "Physics", "7C", "2025-11-13 09:00", "2025-11-13 09:45", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202511130900_202511130945_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ma_7a_202511131000_202511131045_dur_45_rm_a101", "Mathematics", "7A", "2025-11-13 10:00", "2025-11-13 10:45", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202511131000_202511131045_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ma_8c_202511131100_202511131145_dur_45_rm_a103", "Mathematics", "8C", "2025-11-13 11:00", "2025-11-13 11:45", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202511131100_202511131145_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202511131230_202511131315_dur_45_rm_a102", "Mathematics", "7B", "2025-11-13 12:30", "2025-11-13 13:15", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202511131230_202511131315_dur_45_rm_a102");

    INSERT INTO Class VALUES("cl_ph_9b_202511200815_202511200900_dur_45_rm_gym1", "Physics", "9B", "2025-11-20 08:15", "2025-11-20 09:00", "45", "Gym1", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202511200815_202511200900_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ph_7c_202511200900_202511200945_dur_45_rm_a104", "Physics", "7C", "2025-11-20 09:00", "2025-11-20 09:45", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202511200900_202511200945_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ma_7a_202511201000_202511201045_dur_45_rm_a101", "Mathematics", "7A", "2025-11-20 10:00", "2025-11-20 10:45", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202511201000_202511201045_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ma_8c_202511201100_202511201145_dur_45_rm_a103", "Mathematics", "8C", "2025-11-20 11:00", "2025-11-20 11:45", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202511201100_202511201145_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202511201230_202511201315_dur_45_rm_a102", "Mathematics", "7B", "2025-11-20 12:30", "2025-11-20 13:15", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202511201230_202511201315_dur_45_rm_a102");

    INSERT INTO Class VALUES("cl_ph_9b_202511270815_202511270900_dur_45_rm_gym1", "Physics", "9B", "2025-11-27 08:15", "2025-11-27 09:00", "45", "Gym1", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202511270815_202511270900_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ph_7c_202511270900_202511270945_dur_45_rm_a104", "Physics", "7C", "2025-11-27 09:00", "2025-11-27 09:45", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202511270900_202511270945_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ma_7a_202511271000_202511271045_dur_45_rm_a101", "Mathematics", "7A", "2025-11-27 10:00", "2025-11-27 10:45", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202511271000_202511271045_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ma_8c_202511271100_202511271145_dur_45_rm_a103", "Mathematics", "8C", "2025-11-27 11:00", "2025-11-27 11:45", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202511271100_202511271145_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202511271230_202511271315_dur_45_rm_a102", "Mathematics", "7B", "2025-11-27 12:30", "2025-11-27 13:15", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202511271230_202511271315_dur_45_rm_a102");

    INSERT INTO Class VALUES("cl_ph_9b_202512040815_202512040900_dur_45_rm_gym1", "Physics", "9B", "2025-12-04 08:15", "2025-12-04 09:00", "45", "Gym1", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202512040815_202512040900_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ph_7c_202512040900_202512040945_dur_45_rm_a104", "Physics", "7C", "2025-12-04 09:00", "2025-12-04 09:45", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202512040900_202512040945_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ma_7a_202512041000_202512041045_dur_45_rm_a101", "Mathematics", "7A", "2025-12-04 10:00", "2025-12-04 10:45", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202512041000_202512041045_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ma_8c_202512041100_202512041145_dur_45_rm_a103", "Mathematics", "8C", "2025-12-04 11:00", "2025-12-04 11:45", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202512041100_202512041145_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202512041230_202512041315_dur_45_rm_a102", "Mathematics", "7B", "2025-12-04 12:30", "2025-12-04 13:15", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202512041230_202512041315_dur_45_rm_a102");

    INSERT INTO Class VALUES("cl_ph_9b_202512110815_202512110900_dur_45_rm_gym1", "Physics", "9B", "2025-12-11 08:15", "2025-12-11 09:00", "45", "Gym1", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202512110815_202512110900_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ph_7c_202512110900_202512110945_dur_45_rm_a104", "Physics", "7C", "2025-12-11 09:00", "2025-12-11 09:45", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202512110900_202512110945_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ma_7a_202512111000_202512111045_dur_45_rm_a101", "Mathematics", "7A", "2025-12-11 10:00", "2025-12-11 10:45", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202512111000_202512111045_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ma_8c_202512111100_202512111145_dur_45_rm_a103", "Mathematics", "8C", "2025-12-11 11:00", "2025-12-11 11:45", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202512111100_202512111145_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202512111230_202512111315_dur_45_rm_a102", "Mathematics", "7B", "2025-12-11 12:30", "2025-12-11 13:15", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202512111230_202512111315_dur_45_rm_a102");

    INSERT INTO Class VALUES("cl_ph_9b_202512180815_202512180900_dur_45_rm_gym1", "Physics", "9B", "2025-12-18 08:15", "2025-12-18 09:00", "45", "Gym1", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202512180815_202512180900_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ph_7c_202512180900_202512180945_dur_45_rm_a104", "Physics", "7C", "2025-12-18 09:00", "2025-12-18 09:45", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202512180900_202512180945_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ma_7a_202512181000_202512181045_dur_45_rm_a101", "Mathematics", "7A", "2025-12-18 10:00", "2025-12-18 10:45", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202512181000_202512181045_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ma_8c_202512181100_202512181145_dur_45_rm_a103", "Mathematics", "8C", "2025-12-18 11:00", "2025-12-18 11:45", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202512181100_202512181145_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202512181230_202512181315_dur_45_rm_a102", "Mathematics", "7B", "2025-12-18 12:30", "2025-12-18 13:15", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202512181230_202512181315_dur_45_rm_a102");

    INSERT INTO Class VALUES("cl_ph_9b_202512250815_202512250900_dur_45_rm_gym1", "Physics", "9B", "2025-12-25 08:15", "2025-12-25 09:00", "45", "Gym1", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202512250815_202512250900_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ph_7c_202512250900_202512250945_dur_45_rm_a104", "Physics", "7C", "2025-12-25 09:00", "2025-12-25 09:45", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202512250900_202512250945_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ma_7a_202512251000_202512251045_dur_45_rm_a101", "Mathematics", "7A", "2025-12-25 10:00", "2025-12-25 10:45", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202512251000_202512251045_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ma_8c_202512251100_202512251145_dur_45_rm_a103", "Mathematics", "8C", "2025-12-25 11:00", "2025-12-25 11:45", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202512251100_202512251145_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202512251230_202512251315_dur_45_rm_a102", "Mathematics", "7B", "2025-12-25 12:30", "2025-12-25 13:15", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202512251230_202512251315_dur_45_rm_a102");

    INSERT INTO Class VALUES("cl_ph_9b_202601010815_202601010900_dur_45_rm_gym1", "Physics", "9B", "2026-01-01 08:15", "2026-01-01 09:00", "45", "Gym1", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202601010815_202601010900_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ph_7c_202601010900_202601010945_dur_45_rm_a104", "Physics", "7C", "2026-01-01 09:00", "2026-01-01 09:45", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202601010900_202601010945_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ma_7a_202601011000_202601011045_dur_45_rm_a101", "Mathematics", "7A", "2026-01-01 10:00", "2026-01-01 10:45", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202601011000_202601011045_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ma_8c_202601011100_202601011145_dur_45_rm_a103", "Mathematics", "8C", "2026-01-01 11:00", "2026-01-01 11:45", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202601011100_202601011145_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202601011230_202601011315_dur_45_rm_a102", "Mathematics", "7B", "2026-01-01 12:30", "2026-01-01 13:15", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202601011230_202601011315_dur_45_rm_a102");

    INSERT INTO Class VALUES("cl_ph_9b_202601080815_202601080900_dur_45_rm_gym1", "Physics", "9B", "2026-01-08 08:15", "2026-01-08 09:00", "45", "Gym1", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202601080815_202601080900_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ph_7c_202601080900_202601080945_dur_45_rm_a104", "Physics", "7C", "2026-01-08 09:00", "2026-01-08 09:45", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202601080900_202601080945_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ma_7a_202601081000_202601081045_dur_45_rm_a101", "Mathematics", "7A", "2026-01-08 10:00", "2026-01-08 10:45", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202601081000_202601081045_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ma_8c_202601081100_202601081145_dur_45_rm_a103", "Mathematics", "8C", "2026-01-08 11:00", "2026-01-08 11:45", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202601081100_202601081145_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202601081230_202601081315_dur_45_rm_a102", "Mathematics", "7B", "2026-01-08 12:30", "2026-01-08 13:15", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202601081230_202601081315_dur_45_rm_a102");

    INSERT INTO Class VALUES("cl_ph_9b_202601150815_202601150900_dur_45_rm_gym1", "Physics", "9B", "2026-01-15 08:15", "2026-01-15 09:00", "45", "Gym1", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202601150815_202601150900_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ph_7c_202601150900_202601150945_dur_45_rm_a104", "Physics", "7C", "2026-01-15 09:00", "2026-01-15 09:45", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202601150900_202601150945_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ma_7a_202601151000_202601151045_dur_45_rm_a101", "Mathematics", "7A", "2026-01-15 10:00", "2026-01-15 10:45", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202601151000_202601151045_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ma_8c_202601151100_202601151145_dur_45_rm_a103", "Mathematics", "8C", "2026-01-15 11:00", "2026-01-15 11:45", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202601151100_202601151145_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202601151230_202601151315_dur_45_rm_a102", "Mathematics", "7B", "2026-01-15 12:30", "2026-01-15 13:15", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202601151230_202601151315_dur_45_rm_a102");

    INSERT INTO Class VALUES("cl_ph_9b_202601220815_202601220900_dur_45_rm_gym1", "Physics", "9B", "2026-01-22 08:15", "2026-01-22 09:00", "45", "Gym1", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202601220815_202601220900_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ph_7c_202601220900_202601220945_dur_45_rm_a104", "Physics", "7C", "2026-01-22 09:00", "2026-01-22 09:45", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202601220900_202601220945_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ma_7a_202601221000_202601221045_dur_45_rm_a101", "Mathematics", "7A", "2026-01-22 10:00", "2026-01-22 10:45", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202601221000_202601221045_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ma_8c_202601221100_202601221145_dur_45_rm_a103", "Mathematics", "8C", "2026-01-22 11:00", "2026-01-22 11:45", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202601221100_202601221145_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202601221230_202601221315_dur_45_rm_a102", "Mathematics", "7B", "2026-01-22 12:30", "2026-01-22 13:15", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202601221230_202601221315_dur_45_rm_a102");

    INSERT INTO Class VALUES("cl_ph_9b_202601290815_202601290900_dur_45_rm_gym1", "Physics", "9B", "2026-01-29 08:15", "2026-01-29 09:00", "45", "Gym1", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202601290815_202601290900_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ph_7c_202601290900_202601290945_dur_45_rm_a104", "Physics", "7C", "2026-01-29 09:00", "2026-01-29 09:45", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202601290900_202601290945_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ma_7a_202601291000_202601291045_dur_45_rm_a101", "Mathematics", "7A", "2026-01-29 10:00", "2026-01-29 10:45", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202601291000_202601291045_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ma_8c_202601291100_202601291145_dur_45_rm_a103", "Mathematics", "8C", "2026-01-29 11:00", "2026-01-29 11:45", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202601291100_202601291145_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202601291230_202601291315_dur_45_rm_a102", "Mathematics", "7B", "2026-01-29 12:30", "2026-01-29 13:15", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202601291230_202601291315_dur_45_rm_a102");

    INSERT INTO Class VALUES("cl_ph_9b_202602050815_202602050900_dur_45_rm_gym1", "Physics", "9B", "2026-02-05 08:15", "2026-02-05 09:00", "45", "Gym1", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202602050815_202602050900_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ph_7c_202602050900_202602050945_dur_45_rm_a104", "Physics", "7C", "2026-02-05 09:00", "2026-02-05 09:45", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202602050900_202602050945_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ma_7a_202602051000_202602051045_dur_45_rm_a101", "Mathematics", "7A", "2026-02-05 10:00", "2026-02-05 10:45", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202602051000_202602051045_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ma_8c_202602051100_202602051145_dur_45_rm_a103", "Mathematics", "8C", "2026-02-05 11:00", "2026-02-05 11:45", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202602051100_202602051145_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202602051230_202602051315_dur_45_rm_a102", "Mathematics", "7B", "2026-02-05 12:30", "2026-02-05 13:15", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202602051230_202602051315_dur_45_rm_a102");

    INSERT INTO Class VALUES("cl_ph_9b_202602120815_202602120900_dur_45_rm_gym1", "Physics", "9B", "2026-02-12 08:15", "2026-02-12 09:00", "45", "Gym1", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202602120815_202602120900_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ph_7c_202602120900_202602120945_dur_45_rm_a104", "Physics", "7C", "2026-02-12 09:00", "2026-02-12 09:45", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202602120900_202602120945_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ma_7a_202602121000_202602121045_dur_45_rm_a101", "Mathematics", "7A", "2026-02-12 10:00", "2026-02-12 10:45", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202602121000_202602121045_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ma_8c_202602121100_202602121145_dur_45_rm_a103", "Mathematics", "8C", "2026-02-12 11:00", "2026-02-12 11:45", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202602121100_202602121145_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202602121230_202602121315_dur_45_rm_a102", "Mathematics", "7B", "2026-02-12 12:30", "2026-02-12 13:15", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202602121230_202602121315_dur_45_rm_a102");

    INSERT INTO Class VALUES("cl_ph_9b_202602190815_202602190900_dur_45_rm_gym1", "Physics", "9B", "2026-02-19 08:15", "2026-02-19 09:00", "45", "Gym1", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202602190815_202602190900_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ph_7c_202602190900_202602190945_dur_45_rm_a104", "Physics", "7C", "2026-02-19 09:00", "2026-02-19 09:45", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202602190900_202602190945_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ma_7a_202602191000_202602191045_dur_45_rm_a101", "Mathematics", "7A", "2026-02-19 10:00", "2026-02-19 10:45", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202602191000_202602191045_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ma_8c_202602191100_202602191145_dur_45_rm_a103", "Mathematics", "8C", "2026-02-19 11:00", "2026-02-19 11:45", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202602191100_202602191145_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202602191230_202602191315_dur_45_rm_a102", "Mathematics", "7B", "2026-02-19 12:30", "2026-02-19 13:15", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202602191230_202602191315_dur_45_rm_a102");

    INSERT INTO Class VALUES("cl_ph_9b_202602260815_202602260900_dur_45_rm_gym1", "Physics", "9B", "2026-02-26 08:15", "2026-02-26 09:00", "45", "Gym1", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202602260815_202602260900_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ph_7c_202602260900_202602260945_dur_45_rm_a104", "Physics", "7C", "2026-02-26 09:00", "2026-02-26 09:45", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202602260900_202602260945_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ma_7a_202602261000_202602261045_dur_45_rm_a101", "Mathematics", "7A", "2026-02-26 10:00", "2026-02-26 10:45", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202602261000_202602261045_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ma_8c_202602261100_202602261145_dur_45_rm_a103", "Mathematics", "8C", "2026-02-26 11:00", "2026-02-26 11:45", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202602261100_202602261145_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202602261230_202602261315_dur_45_rm_a102", "Mathematics", "7B", "2026-02-26 12:30", "2026-02-26 13:15", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202602261230_202602261315_dur_45_rm_a102");

    INSERT INTO Class VALUES("cl_ph_9b_202603050815_202603050900_dur_45_rm_gym1", "Physics", "9B", "2026-03-05 08:15", "2026-03-05 09:00", "45", "Gym1", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202603050815_202603050900_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ph_7c_202603050900_202603050945_dur_45_rm_a104", "Physics", "7C", "2026-03-05 09:00", "2026-03-05 09:45", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202603050900_202603050945_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ma_7a_202603051000_202603051045_dur_45_rm_a101", "Mathematics", "7A", "2026-03-05 10:00", "2026-03-05 10:45", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202603051000_202603051045_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ma_8c_202603051100_202603051145_dur_45_rm_a103", "Mathematics", "8C", "2026-03-05 11:00", "2026-03-05 11:45", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202603051100_202603051145_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202603051230_202603051315_dur_45_rm_a102", "Mathematics", "7B", "2026-03-05 12:30", "2026-03-05 13:15", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202603051230_202603051315_dur_45_rm_a102");

    INSERT INTO Class VALUES("cl_ph_9b_202603120815_202603120900_dur_45_rm_gym1", "Physics", "9B", "2026-03-12 08:15", "2026-03-12 09:00", "45", "Gym1", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202603120815_202603120900_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ph_7c_202603120900_202603120945_dur_45_rm_a104", "Physics", "7C", "2026-03-12 09:00", "2026-03-12 09:45", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202603120900_202603120945_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ma_7a_202603121000_202603121045_dur_45_rm_a101", "Mathematics", "7A", "2026-03-12 10:00", "2026-03-12 10:45", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202603121000_202603121045_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ma_8c_202603121100_202603121145_dur_45_rm_a103", "Mathematics", "8C", "2026-03-12 11:00", "2026-03-12 11:45", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202603121100_202603121145_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202603121230_202603121315_dur_45_rm_a102", "Mathematics", "7B", "2026-03-12 12:30", "2026-03-12 13:15", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202603121230_202603121315_dur_45_rm_a102");

    INSERT INTO Class VALUES("cl_ph_9b_202603190815_202603190900_dur_45_rm_gym1", "Physics", "9B", "2026-03-19 08:15", "2026-03-19 09:00", "45", "Gym1", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202603190815_202603190900_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ph_7c_202603190900_202603190945_dur_45_rm_a104", "Physics", "7C", "2026-03-19 09:00", "2026-03-19 09:45", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202603190900_202603190945_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ma_7a_202603191000_202603191045_dur_45_rm_a101", "Mathematics", "7A", "2026-03-19 10:00", "2026-03-19 10:45", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202603191000_202603191045_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ma_8c_202603191100_202603191145_dur_45_rm_a103", "Mathematics", "8C", "2026-03-19 11:00", "2026-03-19 11:45", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202603191100_202603191145_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202603191230_202603191315_dur_45_rm_a102", "Mathematics", "7B", "2026-03-19 12:30", "2026-03-19 13:15", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202603191230_202603191315_dur_45_rm_a102");

    INSERT INTO Class VALUES("cl_ph_9b_202603260815_202603260900_dur_45_rm_gym1", "Physics", "9B", "2026-03-26 08:15", "2026-03-26 09:00", "45", "Gym1", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_9b_202603260815_202603260900_dur_45_rm_gym1");
    INSERT INTO Class VALUES("cl_ph_7c_202603260900_202603260945_dur_45_rm_a104", "Physics", "7C", "2026-03-26 09:00", "2026-03-26 09:45", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202603260900_202603260945_dur_45_rm_a104");
    INSERT INTO Class VALUES("cl_ma_7a_202603261000_202603261045_dur_45_rm_a101", "Mathematics", "7A", "2026-03-26 10:00", "2026-03-26 10:45", "45", "A101", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7a_202603261000_202603261045_dur_45_rm_a101");
    INSERT INTO Class VALUES("cl_ma_8c_202603261100_202603261145_dur_45_rm_a103", "Mathematics", "8C", "2026-03-26 11:00", "2026-03-26 11:45", "45", "A103", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_8c_202603261100_202603261145_dur_45_rm_a103");
    INSERT INTO Class VALUES("cl_ma_7b_202603261230_202603261315_dur_45_rm_a102", "Mathematics", "7B", "2026-03-26 12:30", "2026-03-26 13:15", "45", "A102", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ma_7b_202603261230_202603261315_dur_45_rm_a102");

    INSERT INTO Class VALUES("cl_ph_8a_202511140815_202511140900_dur_45_rm_a105", "Physics", "8A", "2025-11-14 08:15", "2025-11-14 09:00", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202511140815_202511140900_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ch_8b_202511140900_202511140945_dur_45_rm_b204", "Chemistry", "8B", "2025-11-14 09:00", "2025-11-14 09:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202511140900_202511140945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202511141000_202511141045_dur_45_rm_b205", "Chemistry", "9A", "2025-11-14 10:00", "2025-11-14 10:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202511141000_202511141045_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_7c_202511141100_202511141145_dur_45_rm_a104", "Physics", "7C", "2025-11-14 11:00", "2025-11-14 11:45", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202511141100_202511141145_dur_45_rm_a104");

    INSERT INTO Class VALUES("cl_ph_8a_202511210815_202511210900_dur_45_rm_a105", "Physics", "8A", "2025-11-21 08:15", "2025-11-21 09:00", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202511210815_202511210900_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ch_8b_202511210900_202511210945_dur_45_rm_b204", "Chemistry", "8B", "2025-11-21 09:00", "2025-11-21 09:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202511210900_202511210945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202511211000_202511211045_dur_45_rm_b205", "Chemistry", "9A", "2025-11-21 10:00", "2025-11-21 10:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202511211000_202511211045_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_7c_202511211100_202511211145_dur_45_rm_a104", "Physics", "7C", "2025-11-21 11:00", "2025-11-21 11:45", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202511211100_202511211145_dur_45_rm_a104");

    INSERT INTO Class VALUES("cl_ph_8a_202511280815_202511280900_dur_45_rm_a105", "Physics", "8A", "2025-11-28 08:15", "2025-11-28 09:00", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202511280815_202511280900_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ch_8b_202511280900_202511280945_dur_45_rm_b204", "Chemistry", "8B", "2025-11-28 09:00", "2025-11-28 09:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202511280900_202511280945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202511281000_202511281045_dur_45_rm_b205", "Chemistry", "9A", "2025-11-28 10:00", "2025-11-28 10:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202511281000_202511281045_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_7c_202511281100_202511281145_dur_45_rm_a104", "Physics", "7C", "2025-11-28 11:00", "2025-11-28 11:45", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202511281100_202511281145_dur_45_rm_a104");

    INSERT INTO Class VALUES("cl_ph_8a_202512050815_202512050900_dur_45_rm_a105", "Physics", "8A", "2025-12-05 08:15", "2025-12-05 09:00", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202512050815_202512050900_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ch_8b_202512050900_202512050945_dur_45_rm_b204", "Chemistry", "8B", "2025-12-05 09:00", "2025-12-05 09:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202512050900_202512050945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202512051000_202512051045_dur_45_rm_b205", "Chemistry", "9A", "2025-12-05 10:00", "2025-12-05 10:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202512051000_202512051045_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_7c_202512051100_202512051145_dur_45_rm_a104", "Physics", "7C", "2025-12-05 11:00", "2025-12-05 11:45", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202512051100_202512051145_dur_45_rm_a104");

    INSERT INTO Class VALUES("cl_ph_8a_202512120815_202512120900_dur_45_rm_a105", "Physics", "8A", "2025-12-12 08:15", "2025-12-12 09:00", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202512120815_202512120900_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ch_8b_202512120900_202512120945_dur_45_rm_b204", "Chemistry", "8B", "2025-12-12 09:00", "2025-12-12 09:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202512120900_202512120945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202512121000_202512121045_dur_45_rm_b205", "Chemistry", "9A", "2025-12-12 10:00", "2025-12-12 10:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202512121000_202512121045_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_7c_202512121100_202512121145_dur_45_rm_a104", "Physics", "7C", "2025-12-12 11:00", "2025-12-12 11:45", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202512121100_202512121145_dur_45_rm_a104");

    INSERT INTO Class VALUES("cl_ph_8a_202512190815_202512190900_dur_45_rm_a105", "Physics", "8A", "2025-12-19 08:15", "2025-12-19 09:00", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202512190815_202512190900_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ch_8b_202512190900_202512190945_dur_45_rm_b204", "Chemistry", "8B", "2025-12-19 09:00", "2025-12-19 09:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202512190900_202512190945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202512191000_202512191045_dur_45_rm_b205", "Chemistry", "9A", "2025-12-19 10:00", "2025-12-19 10:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202512191000_202512191045_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_7c_202512191100_202512191145_dur_45_rm_a104", "Physics", "7C", "2025-12-19 11:00", "2025-12-19 11:45", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202512191100_202512191145_dur_45_rm_a104");

    INSERT INTO Class VALUES("cl_ph_8a_202512260815_202512260900_dur_45_rm_a105", "Physics", "8A", "2025-12-26 08:15", "2025-12-26 09:00", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202512260815_202512260900_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ch_8b_202512260900_202512260945_dur_45_rm_b204", "Chemistry", "8B", "2025-12-26 09:00", "2025-12-26 09:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202512260900_202512260945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202512261000_202512261045_dur_45_rm_b205", "Chemistry", "9A", "2025-12-26 10:00", "2025-12-26 10:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202512261000_202512261045_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_7c_202512261100_202512261145_dur_45_rm_a104", "Physics", "7C", "2025-12-26 11:00", "2025-12-26 11:45", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202512261100_202512261145_dur_45_rm_a104");

    INSERT INTO Class VALUES("cl_ph_8a_202601020815_202601020900_dur_45_rm_a105", "Physics", "8A", "2026-01-02 08:15", "2026-01-02 09:00", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202601020815_202601020900_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ch_8b_202601020900_202601020945_dur_45_rm_b204", "Chemistry", "8B", "2026-01-02 09:00", "2026-01-02 09:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202601020900_202601020945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202601021000_202601021045_dur_45_rm_b205", "Chemistry", "9A", "2026-01-02 10:00", "2026-01-02 10:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202601021000_202601021045_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_7c_202601021100_202601021145_dur_45_rm_a104", "Physics", "7C", "2026-01-02 11:00", "2026-01-02 11:45", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202601021100_202601021145_dur_45_rm_a104");

    INSERT INTO Class VALUES("cl_ph_8a_202601090815_202601090900_dur_45_rm_a105", "Physics", "8A", "2026-01-09 08:15", "2026-01-09 09:00", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202601090815_202601090900_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ch_8b_202601090900_202601090945_dur_45_rm_b204", "Chemistry", "8B", "2026-01-09 09:00", "2026-01-09 09:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202601090900_202601090945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202601091000_202601091045_dur_45_rm_b205", "Chemistry", "9A", "2026-01-09 10:00", "2026-01-09 10:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202601091000_202601091045_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_7c_202601091100_202601091145_dur_45_rm_a104", "Physics", "7C", "2026-01-09 11:00", "2026-01-09 11:45", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202601091100_202601091145_dur_45_rm_a104");

    INSERT INTO Class VALUES("cl_ph_8a_202601160815_202601160900_dur_45_rm_a105", "Physics", "8A", "2026-01-16 08:15", "2026-01-16 09:00", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202601160815_202601160900_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ch_8b_202601160900_202601160945_dur_45_rm_b204", "Chemistry", "8B", "2026-01-16 09:00", "2026-01-16 09:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202601160900_202601160945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202601161000_202601161045_dur_45_rm_b205", "Chemistry", "9A", "2026-01-16 10:00", "2026-01-16 10:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202601161000_202601161045_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_7c_202601161100_202601161145_dur_45_rm_a104", "Physics", "7C", "2026-01-16 11:00", "2026-01-16 11:45", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202601161100_202601161145_dur_45_rm_a104");

    INSERT INTO Class VALUES("cl_ph_8a_202601230815_202601230900_dur_45_rm_a105", "Physics", "8A", "2026-01-23 08:15", "2026-01-23 09:00", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202601230815_202601230900_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ch_8b_202601230900_202601230945_dur_45_rm_b204", "Chemistry", "8B", "2026-01-23 09:00", "2026-01-23 09:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202601230900_202601230945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202601231000_202601231045_dur_45_rm_b205", "Chemistry", "9A", "2026-01-23 10:00", "2026-01-23 10:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202601231000_202601231045_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_7c_202601231100_202601231145_dur_45_rm_a104", "Physics", "7C", "2026-01-23 11:00", "2026-01-23 11:45", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202601231100_202601231145_dur_45_rm_a104");

    INSERT INTO Class VALUES("cl_ph_8a_202601300815_202601300900_dur_45_rm_a105", "Physics", "8A", "2026-01-30 08:15", "2026-01-30 09:00", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202601300815_202601300900_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ch_8b_202601300900_202601300945_dur_45_rm_b204", "Chemistry", "8B", "2026-01-30 09:00", "2026-01-30 09:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202601300900_202601300945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202601301000_202601301045_dur_45_rm_b205", "Chemistry", "9A", "2026-01-30 10:00", "2026-01-30 10:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202601301000_202601301045_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_7c_202601301100_202601301145_dur_45_rm_a104", "Physics", "7C", "2026-01-30 11:00", "2026-01-30 11:45", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202601301100_202601301145_dur_45_rm_a104");

    INSERT INTO Class VALUES("cl_ph_8a_202602060815_202602060900_dur_45_rm_a105", "Physics", "8A", "2026-02-06 08:15", "2026-02-06 09:00", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202602060815_202602060900_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ch_8b_202602060900_202602060945_dur_45_rm_b204", "Chemistry", "8B", "2026-02-06 09:00", "2026-02-06 09:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202602060900_202602060945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202602061000_202602061045_dur_45_rm_b205", "Chemistry", "9A", "2026-02-06 10:00", "2026-02-06 10:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202602061000_202602061045_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_7c_202602061100_202602061145_dur_45_rm_a104", "Physics", "7C", "2026-02-06 11:00", "2026-02-06 11:45", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202602061100_202602061145_dur_45_rm_a104");

    INSERT INTO Class VALUES("cl_ph_8a_202602130815_202602130900_dur_45_rm_a105", "Physics", "8A", "2026-02-13 08:15", "2026-02-13 09:00", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202602130815_202602130900_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ch_8b_202602130900_202602130945_dur_45_rm_b204", "Chemistry", "8B", "2026-02-13 09:00", "2026-02-13 09:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202602130900_202602130945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202602131000_202602131045_dur_45_rm_b205", "Chemistry", "9A", "2026-02-13 10:00", "2026-02-13 10:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202602131000_202602131045_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_7c_202602131100_202602131145_dur_45_rm_a104", "Physics", "7C", "2026-02-13 11:00", "2026-02-13 11:45", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202602131100_202602131145_dur_45_rm_a104");

    INSERT INTO Class VALUES("cl_ph_8a_202602200815_202602200900_dur_45_rm_a105", "Physics", "8A", "2026-02-20 08:15", "2026-02-20 09:00", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202602200815_202602200900_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ch_8b_202602200900_202602200945_dur_45_rm_b204", "Chemistry", "8B", "2026-02-20 09:00", "2026-02-20 09:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202602200900_202602200945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202602201000_202602201045_dur_45_rm_b205", "Chemistry", "9A", "2026-02-20 10:00", "2026-02-20 10:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202602201000_202602201045_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_7c_202602201100_202602201145_dur_45_rm_a104", "Physics", "7C", "2026-02-20 11:00", "2026-02-20 11:45", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202602201100_202602201145_dur_45_rm_a104");

    INSERT INTO Class VALUES("cl_ph_8a_202602270815_202602270900_dur_45_rm_a105", "Physics", "8A", "2026-02-27 08:15", "2026-02-27 09:00", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202602270815_202602270900_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ch_8b_202602270900_202602270945_dur_45_rm_b204", "Chemistry", "8B", "2026-02-27 09:00", "2026-02-27 09:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202602270900_202602270945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202602271000_202602271045_dur_45_rm_b205", "Chemistry", "9A", "2026-02-27 10:00", "2026-02-27 10:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202602271000_202602271045_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_7c_202602271100_202602271145_dur_45_rm_a104", "Physics", "7C", "2026-02-27 11:00", "2026-02-27 11:45", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202602271100_202602271145_dur_45_rm_a104");

    INSERT INTO Class VALUES("cl_ph_8a_202603060815_202603060900_dur_45_rm_a105", "Physics", "8A", "2026-03-06 08:15", "2026-03-06 09:00", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202603060815_202603060900_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ch_8b_202603060900_202603060945_dur_45_rm_b204", "Chemistry", "8B", "2026-03-06 09:00", "2026-03-06 09:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202603060900_202603060945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202603061000_202603061045_dur_45_rm_b205", "Chemistry", "9A", "2026-03-06 10:00", "2026-03-06 10:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202603061000_202603061045_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_7c_202603061100_202603061145_dur_45_rm_a104", "Physics", "7C", "2026-03-06 11:00", "2026-03-06 11:45", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202603061100_202603061145_dur_45_rm_a104");

    INSERT INTO Class VALUES("cl_ph_8a_202603130815_202603130900_dur_45_rm_a105", "Physics", "8A", "2026-03-13 08:15", "2026-03-13 09:00", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202603130815_202603130900_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ch_8b_202603130900_202603130945_dur_45_rm_b204", "Chemistry", "8B", "2026-03-13 09:00", "2026-03-13 09:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202603130900_202603130945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202603131000_202603131045_dur_45_rm_b205", "Chemistry", "9A", "2026-03-13 10:00", "2026-03-13 10:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202603131000_202603131045_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_7c_202603131100_202603131145_dur_45_rm_a104", "Physics", "7C", "2026-03-13 11:00", "2026-03-13 11:45", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202603131100_202603131145_dur_45_rm_a104");

    INSERT INTO Class VALUES("cl_ph_8a_202603200815_202603200900_dur_45_rm_a105", "Physics", "8A", "2026-03-20 08:15", "2026-03-20 09:00", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202603200815_202603200900_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ch_8b_202603200900_202603200945_dur_45_rm_b204", "Chemistry", "8B", "2026-03-20 09:00", "2026-03-20 09:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202603200900_202603200945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202603201000_202603201045_dur_45_rm_b205", "Chemistry", "9A", "2026-03-20 10:00", "2026-03-20 10:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202603201000_202603201045_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_7c_202603201100_202603201145_dur_45_rm_a104", "Physics", "7C", "2026-03-20 11:00", "2026-03-20 11:45", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202603201100_202603201145_dur_45_rm_a104");

    INSERT INTO Class VALUES("cl_ph_8a_202603270815_202603270900_dur_45_rm_a105", "Physics", "8A", "2026-03-27 08:15", "2026-03-27 09:00", "45", "A105", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_8a_202603270815_202603270900_dur_45_rm_a105");
    INSERT INTO Class VALUES("cl_ch_8b_202603270900_202603270945_dur_45_rm_b204", "Chemistry", "8B", "2026-03-27 09:00", "2026-03-27 09:45", "45", "B204", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_8b_202603270900_202603270945_dur_45_rm_b204");
    INSERT INTO Class VALUES("cl_ch_9a_202603271000_202603271045_dur_45_rm_b205", "Chemistry", "9A", "2026-03-27 10:00", "2026-03-27 10:45", "45", "B205", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ch_9a_202603271000_202603271045_dur_45_rm_b205");
    INSERT INTO Class VALUES("cl_ph_7c_202603271100_202603271145_dur_45_rm_a104", "Physics", "7C", "2026-03-27 11:00", "2026-03-27 11:45", "45", "A104", "sc_joni");
    INSERT INTO Teaches Values("t_mikavanhamki_joni" , "cl_ph_7c_202603271100_202603271145_dur_45_rm_a104");
    """)
    conn.commit()          # <-- add this
except Exception as e:
    conn.rollback()        # good hygiene
    raise
finally:
    conn.close()
