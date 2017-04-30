--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.2
-- Dumped by pg_dump version 9.6.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: course; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE course (
    course_code character(8) NOT NULL,
    title character varying(100),
    description text,
    raw_prerequisites text,
    units integer,
    course_profile_id integer,
    semester_1 boolean,
    semester_2 boolean,
    summer_semester boolean,
    invalid boolean NOT NULL
);


ALTER TABLE course OWNER TO postgres;

--
-- Name: incompatible_courses; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE incompatible_courses (
    course_code character varying(8) NOT NULL,
    incompatible_course_code character varying(8) NOT NULL
);


ALTER TABLE incompatible_courses OWNER TO postgres;

--
-- Name: plan; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE plan (
    plan_code character(10) NOT NULL,
    program_code character(4) NOT NULL,
    title character(100) NOT NULL
);


ALTER TABLE plan OWNER TO postgres;

--
-- Name: plan_course_list; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE plan_course_list (
    course_code character(8) NOT NULL,
    plan_code character(10) NOT NULL,
    required boolean
);


ALTER TABLE plan_course_list OWNER TO postgres;

--
-- Name: program; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE program (
    program_code character(4) NOT NULL,
    title character(100),
    level character(45),
    abbreviation character(20),
    duration_years integer,
    units integer
);


ALTER TABLE program OWNER TO postgres;

--
-- Name: program_course_list; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE program_course_list (
    course_code character(8) NOT NULL,
    program_code character(4) NOT NULL
);


ALTER TABLE program_course_list OWNER TO postgres;

--
-- Name: course course_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY course
    ADD CONSTRAINT course_pkey PRIMARY KEY (course_code);


--
-- Name: incompatible_courses incompatible_courses_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY incompatible_courses
    ADD CONSTRAINT incompatible_courses_pkey PRIMARY KEY (course_code, incompatible_course_code);


--
-- Name: plan_course_list plan_course_list_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY plan_course_list
    ADD CONSTRAINT plan_course_list_pkey PRIMARY KEY (course_code, plan_code);


--
-- Name: plan planpk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY plan
    ADD CONSTRAINT planpk PRIMARY KEY (plan_code);


--
-- Name: program_course_list program_course_list_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY program_course_list
    ADD CONSTRAINT program_course_list_pkey PRIMARY KEY (course_code, program_code);


--
-- Name: program program_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY program
    ADD CONSTRAINT program_pkey PRIMARY KEY (program_code);


--
-- Name: plan_course_list course.course_code; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY plan_course_list
    ADD CONSTRAINT "course.course_code" FOREIGN KEY (course_code) REFERENCES course(course_code);


--
-- Name: incompatible_courses course_code_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY incompatible_courses
    ADD CONSTRAINT course_code_fk FOREIGN KEY (course_code) REFERENCES course(course_code);


--
-- Name: program_course_list coursecodefk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY program_course_list
    ADD CONSTRAINT coursecodefk FOREIGN KEY (course_code) REFERENCES course(course_code);


--
-- Name: incompatible_courses i_course_code_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY incompatible_courses
    ADD CONSTRAINT i_course_code_fk FOREIGN KEY (incompatible_course_code) REFERENCES course(course_code);


--
-- Name: plan_course_list plancodefk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY plan_course_list
    ADD CONSTRAINT plancodefk FOREIGN KEY (plan_code) REFERENCES plan(plan_code);


--
-- Name: program_course_list programcodefk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY program_course_list
    ADD CONSTRAINT programcodefk FOREIGN KEY (program_code) REFERENCES program(program_code);


--
-- PostgreSQL database dump complete
--

