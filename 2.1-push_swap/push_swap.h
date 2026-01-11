/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/10 15:28:17 by meldemir          #+#    #+#             */
/*   Updated: 2026/01/10 15:28:19 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include <stdlib.h>
# include <unistd.h>
# include "libft/libft.h"
# include "libft/ft_printf.h"

# define DEBUG 1

void ft_sa(t_list **stack_a);
void ft_pa(t_list **stack_a, t_list **stack_b);
void ft_ra(t_list **stack_a);
void ft_rra(t_list **stack_a);
/*****************************************************/
void ft_sb(t_list **stack_b);
void ft_pb(t_list **stack_a, t_list **stack_b);
void ft_rb(t_list **stack_b);
void ft_rrb(t_list **stack_b);
/*****************************************************/
void    ft_ss(t_list **stack_a, t_list **stack_b);
void   ft_rr(t_list **stack_a, t_list **stack_b);
void    ft_rrr(t_list **stack_a, t_list **stack_b);
/*****************************************************/
void ft_sort_three(t_list **stack);

#endif