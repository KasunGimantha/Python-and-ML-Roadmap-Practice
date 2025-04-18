package com.library.library_system.model;

import jakarta.persistence.*;
import lombok.*;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;

@Entity //Marks the JPA entry
@Data //generate getters,setters
@NoArgsConstructor //generate a no args constructoir
@AllArgsConstructor //generate an all args constructor
@Builder  //enable builder pattern for the clas

public class Book {
    @Id //Specify the primary key
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    @NotBlank(message = "Title cannot be blank")
    private String title;

    @Column(nullable = false)
    @NotBlank(message = "Author cannot be blank")
    private String author;

    @Column(unique = true)
    private String isbn;

    @Column(nullable = false)
    @NotNull(message = "Status cannot be null")
    private String status = "Available";

}
