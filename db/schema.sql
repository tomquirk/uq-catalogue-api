--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.1
-- Dumped by pg_dump version 9.6.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: course; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE course (
    course_code character(8) NOT NULL,
    title character varying(100) NOT NULL,
    description text NOT NULL,
    raw_prerequisites text NOT NULL,
    units integer NOT NULL,
    course_profile_id integer NOT NULL,
    semester_1 boolean,
    semester_2 boolean,
    summer_semester boolean
);


--
-- Name: plan; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE plan (
    plan_code character(10) NOT NULL,
    program_code character(4) NOT NULL,
    title character(100) NOT NULL
);


--
-- Name: plan_course_list; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE plan_course_list (
    course_code character(8) NOT NULL,
    plan_code character(10) NOT NULL,
    required boolean
);


--
-- Name: program; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE program (
    program_code character(4) NOT NULL,
    title character(100),
    level character(45),
    abbreviation character(20),
    duration_years integer,
    units integer
);


--
-- Name: program_course_list; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE program_course_list (
    course_code character(8) NOT NULL,
    program_code character(4) NOT NULL
);


--
-- Name: course course_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY course
    ADD CONSTRAINT course_pkey PRIMARY KEY (course_code);


--
-- Name: plan_course_list plan_course_list_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY plan_course_list
    ADD CONSTRAINT plan_course_list_pkey PRIMARY KEY (course_code, plan_code);


--
-- Name: plan planpk; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY plan
    ADD CONSTRAINT planpk PRIMARY KEY (plan_code);


--
-- Name: program_course_list program_course_list_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY program_course_list
    ADD CONSTRAINT program_course_list_pkey PRIMARY KEY (course_code, program_code);


--
-- Name: program program_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY program
    ADD CONSTRAINT program_pkey PRIMARY KEY (program_code);


--
-- Name: plan_course_list course.course_code; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY plan_course_list
    ADD CONSTRAINT "course.course_code" FOREIGN KEY (course_code) REFERENCES course(course_code);


--
-- Name: program_course_list coursecodefk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY program_course_list
    ADD CONSTRAINT coursecodefk FOREIGN KEY (course_code) REFERENCES course(course_code);


--
-- Name: plan_course_list plancodefk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY plan_course_list
    ADD CONSTRAINT plancodefk FOREIGN KEY (plan_code) REFERENCES plan(plan_code);


--
-- Name: program_course_list programcodefk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY program_course_list
    ADD CONSTRAINT programcodefk FOREIGN KEY (program_code) REFERENCES program(program_code);


--
-- PostgreSQL database dump complete
--

